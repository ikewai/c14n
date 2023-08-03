#!/bin/bash
echo "[task.sh] [1/4] Starting Execution."
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

echo "[task.sh] [2/4] Mapping Airtemp data on the monthly timeframe."
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/
echo "---monthly_map_wget.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_map_wget.py $AGGREGATION_DATE
echo "---update_monthly_predictor.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/update_monthly_predictor.py $AGGREGATION_DATE
echo "---monthly_map_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_map_wrapper.py $AGGREGATION_DATE
echo "---monthly_meta_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_meta_wrapper.py $AGGREGATION_DATE
echo "---monthly_state_wrapper.py---"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_state_wrapper.py $AGGREGATION_DATE
echo "---monthly_stn_data.py--- on Tmax"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_stn_data.py Tmax $AGGREGATION_DATE
echo "---monthly_stn_data.py--- on Tmin"
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/monthly/code/monthly_stn_data.py Tmin $AGGREGATION_DATE
echo "[task.sh] [3/4] Preparing to upload data."
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json $AGGREGATION_DATE
python3 add_upload_list_to_config.py upload_config_datestrings_loaded.json config.json $AGGREGATION_DATE
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [4/4] Uploading data."
python3 upload.py

echo "[task.sh] All done!"
