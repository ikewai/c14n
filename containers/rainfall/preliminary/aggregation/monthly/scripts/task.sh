#!/bin/bash
echo "[task.sh] [1/8] Starting Execution."

echo "[task.sh] [2/8] Acquiring and decompressing Monthly Dependencies Archive."
cd /home/hawaii_climate_products_container/preliminary/rainfall/dependencies
# temporary link, will be replaced with a gateway/CDN link when ready
wget https://f000.backblazeb2.com/file/ikewai/monthly_dependencies.zip
unzip monthly_dependencies.zip
rm daily_dependencies.tar.gz

echo "[task.sh] [3/8] Acquiring Statewide Partially-filled Daily Rainfall data for this month."
bash /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/bash/monthly_rf_wget.sh

echo "[task.sh] [4/8] Aggregating Rainfall data on the monthly timeframe."
cd /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly
echo "---daily_to_monthly_agg_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/daily_to_monthly_agg_FINAL.R
echo "---monthly_rf_krig_map_makr_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/monthly_rf_krig_map_makr_FINAL.R

echo "[task.sh] [5/8] Preparing to upload intermediate products."
cd /sync
python3 update_date_string_in_config.py intermediate_products.json intermediate_products_datestrings_loaded.json
python3 add_upload_list_to_config.py intermediate_products_datestrings_loaded.json intermediate_products_config.json
python3 add_auth_info_to_config.py intermediate_products_config.json

echo "[task.sh] [6/8] Attempting to upload the intermediate files."
python3 upload.py intermediate_products_config.json

echo "[task.sh] [7/8] Preparing to upload final products."
cd /sync
python3 update_date_string_in_config.py final_products.json final_products_datestrings_loaded.json
python3 add_upload_list_to_config.py final_products_datestrings_loaded.json final_products_config.json
python3 add_auth_info_to_config.py final_products_config.json

echo "[task.sh] [8/8] Attempting to upload the final files."
python3 upload.py final_products_config.json


echo "[task.sh] All done!"