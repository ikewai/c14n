#!/bin/bash
echo "[task.sh] [1/5] Starting Execution."
export TZ="HST"
echo "It is currently $(date)."
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

echo "[task.sh] [2/5] Aggregating Airtemp data on the daily timeframe."
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/code
echo "---temp_agg_wget.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_agg_wget.py $AGGREGATION_DATE
echo "---hads_temp_parse.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/hads_temp_parse.py $AGGREGATION_DATE
echo "---madis_temp_parse.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/madis_temp_parse.py $AGGREGATION_DATE
echo "---air_temp_aggregate_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/air_temp_aggregate_wrapper.py $AGGREGATION_DATE

echo "[task.sh] [3/5] Mapping Airtemp data on the daily timeframe."
cd /home/hawaii_climate_products_container/
echo "---temp_map_wget.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_map_wget.py $AGGREGATION_DATE
cp -rf dependencies/* /home/hawaii_climate_products_container/preliminary/air_temp/daily/dependencies

cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/
echo "---update_predictor_table.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/update_predictor_table.py $AGGREGATION_DATE
echo "---county_map_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/county_map_wrapper.py $AGGREGATION_DATE
echo "---meta_data_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/meta_data_wrapper.py $AGGREGATION_DATE
echo "---state_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/state_wrapper.py $AGGREGATION_DATE

echo "[task.sh] [4/5] Preparing to upload data."
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json $AGGREGATION_DATE
python3 add_upload_list_to_config.py upload_config_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [5/5] Uploading data."
python3 upload.py

echo "[task.sh] All done!"
