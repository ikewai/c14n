## Air Temperature Aggregation Containers

These containers handle the processes of aggregating, quality-controlling, and mapping air temperature data, which is originally collected by the [data acquisition containers](containers/shared/acquisition).

Contents:
* [`base`](containers/airtemp/aggregation/base): Essential libraries, scripts, and directory setup.
* [`daily`](containers/airtemp/aggregation/daily): Daily aggregation and mapping.
* [`monthly`](containers/airtemp/aggregation/monthly): Monthly aggregation and mapping.

## Usage
The daily and monthly workflows use the same environment parameters:

```sh
# required, for upload capabilities
IW_USERNAME=gateway_username
IW_PASSWORD=gateway_password
IW_API_KEY=gateway_api_key
IW_API_SECRET=gateway_api_secret
# optional, for telling the scripts to aggregate at a specific date
CUSTOM_TIME="2023-03-01"
```

For an interactive run, execute the container with:
```sh
host> docker run --env-file=/path/to/good_env_file.env -it ghcr.io/ikewai/task-at-pre-agg-daily bash
container> cd /actor
container> bash task.sh
```

Or for a typical cron-based run:
```sh
host> docker run --env-file=/path/to/good_env_file.env ghcr.io/ikewai/task-at-pre-agg-daily:prod > /home/someone/at_daily_agg_$(date +\%FT\%H\%M).log
```