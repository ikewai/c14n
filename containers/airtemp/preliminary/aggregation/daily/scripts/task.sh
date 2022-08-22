#!/bin/bash
echo "[task.sh] Starting Execution."

echo "[task.sh] Aggregating Airtemp data on the daily timeframe."
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/code
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_agg_wget.py
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/hads_temp_parse.py
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/madis_temp_parse.py
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/air_temp_aggregate_wrapper.py

echo "[task.sh] Mapping Airtemp data on the daily timeframe."
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_map_wget.py
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/update_predictor_table.py
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/county_map_wrapper.py
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/meta_data_wrapper.py
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/state_wrapper.py

echo "[task.sh] [disabled] Preparing to upload data."
cd /sync
#python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
#python3 upload_list_inserter.py upload_config_datestrings_loaded.json config.json
#python3 upload_auth_injector.py config.json
echo "[task.sh] [disabled] Uploading data."
#python3 upload.py

echo "[task.sh] All done!"