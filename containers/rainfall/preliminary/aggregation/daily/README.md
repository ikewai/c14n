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
docker run --env-file=an_env_file.env ikewai/task-rf-pre-agg-daily:prod > rf_daily_aggregation_output.log` 2>&1
```

## Development Info

### Build-Time
This container does the following tasks to complete the build.
TODO add tasks

### Run-Time
TODO finish URLs and script explanations
This container executes the following, in order, as part of its [`task.sh`](/scripts/task.sh) routine.
* [`hads_daily_rf_FINAL.R`](): (what the script does)
* [`nws_rr5_daily_rf_FINAL.R`](): (what the script does)
* [`madis_daily_rf_FINAL.R`](): (what the script does)
* [`all_data_daily_merge_table_rf_FINAL.R`](): (what the script does)
* [`qaqc_randfor_bad_data_flag_remove_rf_FINAL.R`](): (what the script does)
* [`daily_gap_fill_NR_only_rf_FINAL.R`](): (what the script does)