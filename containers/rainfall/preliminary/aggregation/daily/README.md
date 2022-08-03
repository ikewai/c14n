## Daily Rainfall Aggregation

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