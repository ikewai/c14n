#!/bin/bash
CONDA_CMD="/root/anaconda3/bin/conda run --no-capture-output -n container_env"
echo "[task.sh] [1/5] Starting Execution."

echo "[task.sh] [2/5] Acquiring Daily Dependencies."
cd /home/hawaii_climate_products_container/preliminary/rainfall/dependencies
wget https://ikeauth.its.hawaii.edu/files/v2/download/public/system/ikewai-annotated-data/HCDP/rainfall/HCDP_dependicies/daily_dependencies.tar.gz
tar -xf daily_dependencies.tar.gz
rm daily_dependencies.tar.gz

echo "[task.sh] [3/5] Aggregating Rainfall data on the daily timeframe."
cd /home/hawaii_climate_products_container/preliminary/rainfall/code/daily
$CONDA_CMD Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/hads_daily_rf_FINAL.R
$CONDA_CMD Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/nws_rr5_daily_rf_FINAL.R
$CONDA_CMD Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/madis_daily_rf_FINAL.R
$CONDA_CMD Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/all_data_daily_merge_table_rf_FINAL.R
$CONDA_CMD Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/qaqc_randfor_bad_data_flag_remove_rf_FINAL.R
$CONDA_CMD Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/daily_gap_fill_NR_only_rf_FINAL.R

echo "[task.sh] [4/5] Preparing for upload."
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 add_upload_list_to_config.py upload_config_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [5/5] Attempting to upload the aggregated data."
python3 upload.py

echo "[task.sh] All done!"