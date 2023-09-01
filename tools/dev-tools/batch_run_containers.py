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
#   ]
# }

# The script will run the container for each date, in series.

import argparse
import json
import os
import subprocess
import sys

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

    for date in dates:
        print(f'Running container {container} with AGGREGATION_DATE={date}')
        if not args.dry_run:
            subprocess.run(['docker', 'run', f'--env-file={base_env}', '-e', f'AGGREGATION_DATE={date}', container], check=True)

if __name__ == '__main__':
    main()