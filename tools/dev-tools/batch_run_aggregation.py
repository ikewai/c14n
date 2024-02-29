# This script runs a container repeatedly with the given list of AGGREGATION_DATE env vars and the base env var file.
# currently, this is intended for use with aggregation images (e.g. ghcr.io/ikewai/task-rf-pre-agg-daily:latest)
# with the variable being the AGGREGATION_DATE.

# The data to execute with will be formatted in JSON, like so:
# {
#   "container": "ghcr.io/ikewai/task-rf-pre-agg-daily:latest",
#   "base_env": "/path/to/env_file.env",
#   "dates": [
#     "2023-01-01",
#     "2023-01-02",
#     "2023-01-03"
#   ],
#   "date_ranges": [
#     "2023-01-01_2023-01-05",
#     "2023-01-06_2023-01-10"
#   ]
# }

# The script will run the container for each date, in series.

import argparse
import json
import subprocess
from datetime import datetime, timedelta

def parse_date_range(date_range):
    start_date, end_date = date_range.split('_')
    return start_date, end_date

def generate_dates(start_date, end_date):
    dates = []
    current_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')
    while current_date <= end_date:
        dates.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    return dates

def main():
    parser = argparse.ArgumentParser(description='Run a container repeatedly with the given list of AGGREGATION_DATE env vars.')
    parser.add_argument('data', help='JSON file specifying the container, base env file, and dates to run with')
    parser.add_argument('-d', '--dry-run', action='store_true', help='Do not run the container, just print the commands that would be run')
    args = parser.parse_args()

    with open(args.data) as f:
        data = json.load(f)

    container = data['container']
    base_env = data['base_env']
    dates = data['dates']
    date_ranges = data.get('date_ranges', [])

    for date in dates:
        print(f'Running container {container} with AGGREGATION_DATE={date} and base env file {base_env} at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        if not args.dry_run:
            subprocess.run(['docker', 'run', '-d', '--name=batch_agg', f'--env-file={base_env}', '-e', f'AGGREGATION_DATE={date}', container], check=True, stderr=subprocess.STDOUT)
            subprocess.run(['docker', 'wait', 'batch_agg'], check=True, stderr=subprocess.STDOUT)
            subprocess.run(['docker', 'rm', 'batch_agg'], check=True, stderr=subprocess.STDOUT)

    for date_range in date_ranges:
        start_date, end_date = parse_date_range(date_range)
        dates = generate_dates(start_date, end_date)
        for date in dates:
            print(f'Running container {container} with AGGREGATION_DATE={date} and base env file {base_env} at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            if not args.dry_run:
                subprocess.run(['docker', 'run', '-d', '--name=batch_agg', f'--env-file={base_env}', '-e', f'AGGREGATION_DATE={date}', container], check=True, stderr=subprocess.STDOUT)
                subprocess.run(['docker', 'wait', 'batch_agg'], check=True, stderr=subprocess.STDOUT)
                subprocess.run(['docker', 'rm', 'batch_agg'], check=True, stderr=subprocess.STDOUT)

if __name__ == '__main__':
    main()
