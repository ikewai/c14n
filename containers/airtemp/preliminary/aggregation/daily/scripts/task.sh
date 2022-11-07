#!/bin/bash
echo "[task.sh] [1/5]Starting Execution."

echo "[task.sh] [2/5]Aggregating Airtemp data on the monthly timeframe."
cd /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code


echo "[task.sh] [3/5]Mapping Airtemp data on the monthly timeframe."
cd /home/hawaii_climate_products_container/preliminary/air_temp/monthly/


echo "[task.sh] [4/5]Preparing to upload data."
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 add_upload_list_to_config.py upload_config_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [5/5][disabled] Uploading data."
#python3 upload.py

echo "[task.sh] All done!"