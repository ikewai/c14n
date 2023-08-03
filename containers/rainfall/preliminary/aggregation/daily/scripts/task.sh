#!/bin/bash
echo "[task.sh] [1/8] Starting Execution."
echo "It is currently $(date)."
export TZ="HST"
if [ $AGGREGATION_DATE ]; then
    echo "An aggregation date was provided by the environment."
    echo "Aggregation date is: " $AGGREGATION_DATE
else
    export AGGREGATION_DATE=$(date --iso-8601)
    echo "No aggregation date was provided by the environment. Defaulting to today."
    echo "Aggregation date is: " $AGGREGATION_DATE
fi
export AGGREGATION_DATE_YESTERDAY=$(date --date="$AGGREGATION_DATE - 1 day" --iso-8601)
echo "Yesterday is: " $AGGREGATION_DATE_YESTERDAY

echo "[task.sh] [2/8] Acquiring Daily Dependencies."
cd /home/hawaii_climate_products_container/preliminary/rainfall/dependencies
wget https://ikeauth.its.hawaii.edu/files/v2/download/public/system/ikewai-annotated-data/HCDP/workflow_data/preliminary/rainfall/dependencies/daily_dependencies.tar.gz
tar -xf daily_dependencies.tar.gz
rm daily_dependencies.tar.gz

echo "[task.sh] [3/8] Acquiring yesterday's cumulative aggregation file, if it exists."
cd /home/hawaii_climate_products_container
echo "---rf_daily_wget.sh---"
bash rf_daily_wget.sh

echo "[task.sh] [4/8] Aggregating Rainfall data on the daily timeframe."
cd /home/hawaii_climate_products_container/preliminary/rainfall/code/daily

echo "---begin hads_daily_rf_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/hads_daily_rf_FINAL.R $AGGREGATION_DATE
echo "---end hads_daily_rf_FINAL.R---"
echo "---begin nws_rr5_daily_rf_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/nws_rr5_daily_rf_FINAL.R $AGGREGATION_DATE
echo "---end nws_rr5_daily_rf_FINAL.R---"
echo "---begin madis_daily_rf_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/madis_daily_rf_FINAL.R $AGGREGATION_DATE
echo "---end madis_daily_rf_FINAL.R---"
echo "---begin all_data_daily_merge_table_rf_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/all_data_daily_merge_table_rf_FINAL.R $AGGREGATION_DATE
echo "---end all_data_daily_merge_table_rf_FINAL.R---"
echo "---begin qaqc_randfor_bad_data_flag_remove_rf_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/qaqc_randfor_bad_data_flag_remove_rf_FINAL.R $AGGREGATION_DATE
echo "---end qaqc_randfor_bad_data_flag_remove_rf_FINAL.R---"
echo "---begin daily_gap_fill_NR_only_rf_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/daily_gap_fill_NR_only_rf_FINAL.R $AGGREGATION_DATE
echo "---end daily_gap_fill_NR_only_rf_FINAL.R---"
echo "---begin all_data_daily_last_obs_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/all_data_daily_last_obs_FINAL.R $AGGREGATION_DATE
echo "---end all_data_daily_last_obs_FINAL.R---"

echo "[task.sh] [5/8] Preparing for intermediate data upload."
cd /sync
python3 update_date_string_in_config.py intermediate_upload_config.json intermediate_upload_config_datestrings_loaded.json $AGGREGATION_DATE_YESTERDAY
python3 add_upload_list_to_config.py intermediate_upload_config_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [6/8] Attempting to upload the aggregated intermediate data."
python3 upload.py

echo "[task.sh] [7/8] Preparing for production data upload."
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json $AGGREGATION_DATE_YESTERDAY
python3 add_upload_list_to_config.py upload_config_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [8/8] Attempting to upload the aggregated production data."
python3 upload.py

echo "[task.sh] All done!"
