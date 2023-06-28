## Daily Rainfall Aggregation

## How to Run

In order to successfully run the container, you'll need some environment variables, which can be passed in an env file.
Example:
```sh
# Authentication parameters. All are mandatory.
# A client can be created interactively via agavepy (v2) or tapipy (v3).
IW_USERNAME=username
IW_PASSWORD=password
IW_API_KEY=api_key
IW_API_SECRET=api_secret
```

**Typical production run** (like in a cron schedule)

This executes the container with a specified environment file (see above) and prints both stdout and stderr to the specified log file.
```sh
docker run --env-file=an_env_file.env ghcr.io/ikewai/task-rf-pre-agg-daily:prod > rf_daily_aggregation_output.log 2>&1
```

## Development Info

### Build-Time
This container does the following tasks to complete the build.
- Make directories
- Download workflow scripts from [the rainfall script repo](https://github.com/ikewai/rainfall)
- Download the container's upload config, also from the rainfall script repo
- Copy in task.sh

### Run-Time
TODO finish URLs and script explanations
This container executes the following, in order, as part of its [`task.sh`](/scripts/task.sh) routine.
* [`rf_daily_wget.sh`](https://github.com/ikewai/rainfall/blob/main/code/daily/bash/dailyRFwget.sh): Pulls intermediate data products from the gateway, for things such as building cumulative daily data files.
* [`hads_daily_rf_FINAL.R`](https://github.com/ikewai/rainfall/blob/main/code/daily/rcode/hads_daily_rf_FINAL.R): Aggregates the data acquired from HADS.
* [`nws_rr5_daily_rf_FINAL.R`](https://github.com/ikewai/rainfall/blob/main/code/daily/rcode/nws_rr5_daily_rf_FINAL.R): Aggregates the data acquired from NWS.
* [`madis_daily_rf_FINAL.R`](https://github.com/ikewai/rainfall/blob/main/code/daily/rcode/madis_daily_rf_FINAL.R): Aggregates the data acquired from MADIS.
* [`all_data_daily_merge_table_rf_FINAL.R`](https://github.com/ikewai/rainfall/blob/main/code/daily/rcode/all_data_daily_merge_table_rf_FINAL.R): Merges the data acquired from each source.
* [`qaqc_randfor_bad_data_flag_remove_rf_FINAL.R`](https://github.com/ikewai/rainfall/blob/main/code/daily/rcode/qaqc_randfor_bad_data_flag_remove_rf_FINAL.R): Applies QAQC algorithms to flag and remove bad data.
* [`daily_gap_fill_NR_only_rf_FINAL.R`](https://github.com/ikewai/rainfall/blob/main/code/daily/rcode/daily_gap_fill_NR_only_rf_FINAL.R): Applies gap filling algorithms to fill missing or removed data.
* [`all_data_daily_last_obs_FINAL.R`](https://github.com/ikewai/rainfall/blob/main/code/daily/rcode/all_data_daily_last_obs_FINAL.R): Updates each station in the last-observation file.
