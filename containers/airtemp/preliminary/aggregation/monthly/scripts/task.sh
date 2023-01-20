#!/bin/bash
echo "[task.sh] [1/4] Starting Execution."
export TZ="HST"

echo "[task.sh] [2/4] Mapping Airtemp data on the monthly timeframe."
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/
echo "---monthly_map_wget.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_map_wget.py
echo "---monthly_meta_wget.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/update_monthly_predictor.py
echo "---monthly_map_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_map_wrapper.py
echo "---monthly_meta_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_meta_wrapper.py
echo "---monthly_state_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_state_wrapper.py
echo "---monthly_stn_data.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_stn_data.py

echo "[task.sh] [3/4] Preparing to upload data."
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 add_upload_list_to_config.py upload_config_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [4/4] Uploading data."
python3 upload.py

echo "[task.sh] All done!"