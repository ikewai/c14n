#!/bin/bash
CONDA_CMD="/root/anaconda3/bin/conda run --no-capture-output -n container_env"
echo "[task.sh] [1/6] Starting Execution."

echo "[task.sh] [2/6] Acquiring and decompressing Daily Dependencies Archive."
cd /home/hawaii_climate_products_container/preliminary/rainfall/dependencies
wget https://ikeauth.its.hawaii.edu/files/v2/download/public/system/ikewai-annotated-data/HCDP/rainfall/HCDP_dependicies/daily_dependencies.tar.gz
tar -xf daily_dependencies.tar.gz
rm daily_dependencies.tar.gz

echo "[task.sh] [3/6] Acquiring Statewide Partially-filled Daily Rainfall data for this month."
cd /home/hawaii_climate_products_container/preliminary/rainfall/data_outputs/tables/station_data/daily/partial_filled/statewide
wget https://ikeauth.its.hawaii.edu/files/v2/download/public/system/ikewai-annotated-data/HCDP/production/rainfall/new/day/statewide/partial/station_data/`date +%Y/%m`/rainfall_new_day_statewide_raw_station_data_`date +%Y_%m`.csv \
     -O Statewide_Partial_Filled_Daily_RF_mm_`date +%Y_%m`.csv

echo "[task.sh] [4/6] Aggregating Rainfall data on the monthly timeframe."
cd /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly
$CONDA_CMD Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/daily_to_monthly_agg_FINAL.R
$CONDA_CMD Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/monthly_rf_krig_map_makr_FINAL.R

echo "[task.sh] [5/6] Preparing for upload."
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 add_upload_list_to_config.py upload_config_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [6/6] [disabled] Attempting to upload the aggregated data."
#python3 upload.py

echo "[task.sh] All done!"