#!/bin/bash
echo "[task.sh] [1/5] Starting Execution."

echo "[task.sh] [2/5] Aggregating Airtemp data on the daily timeframe."
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/code
echo "---temp_agg_wget.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_agg_wget.py
echo "---hads_temp_parse.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/hads_temp_parse.py
echo "---madis_temp_parse.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/madis_temp_parse.py
echo "---air_temp_aggregate_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/air_temp_aggregate_wrapper.py

echo "[task.sh] [3/5] Mapping Airtemp data on the daily timeframe."
cd /home/hawaii_climate_products_container/
echo "---temp_map_wget.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_map_wget.py
cp -rf dependencies/* /home/hawaii_climate_products_container/preliminary/air_temp/daily/dependencies

cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/
echo "---update_predictor_table.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/update_predictor_table.py
echo "---county_map_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/county_map_wrapper.py
echo "---meta_data_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/meta_data_wrapper.py
echo "---state_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/state_wrapper.py

echo "[task.sh] [4/5] Preparing to upload data."
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 add_upload_list_to_config.py upload_config_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [5/5] Uploading data."
python3 upload.py

echo "[task.sh] All done!"