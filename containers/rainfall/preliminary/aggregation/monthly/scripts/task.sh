#!/bin/bash
echo "[task.sh] [1/8] Starting Execution."
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

echo "[task.sh] [2/8] Acquiring and decompressing Monthly Dependencies Archive."
cd /home/hawaii_climate_products_container/preliminary/rainfall/dependencies/monthly
wget https://ikeauth.its.hawaii.edu/files/v2/download/public/system/ikewai-annotated-data/HCDP/workflow_data/preliminary/rainfall/dependencies/monthly_dependencies.zip
unzip monthly_dependencies.zip
rm monthly_dependencies.zip

echo "[task.sh] [3/8] Acquiring Statewide Partially-filled Daily Rainfall data for this month."
cd /home/hawaii_climate_products_container/
echo "---monthly_rf_wget.sh---"
bash /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/bash/monthly_rf_wget.sh

echo "[task.sh] [4/8] Aggregating Rainfall data on the monthly timeframe."
cd /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/rcode
echo "---daily_to_monthly_agg_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/rcode/daily_to_monthly_agg_FINAL.R $AGGREGATION_DATE
echo "---monthly_rf_krig_map_makr_FINAL.R---"
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/rcode/monthly_rf_krig_map_makr_FINAL.R $AGGREGATION_DATE

echo "[task.sh] [5/8] Preparing to upload intermediate products."
cd /sync
python3 update_date_string_in_config.py intermediate_products.json intermediate_products_datestrings_loaded.json $AGGREGATION_DATE_YESTERDAY
python3 add_upload_list_to_config.py intermediate_products_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [6/8] Attempting to upload the intermediate files."
python3 upload.py
mv config.json intermediate_products_config.json

echo "[task.sh] [7/8] Preparing to upload final products."
cd /sync
python3 update_date_string_in_config.py final_products.json final_products_datestrings_loaded.json $AGGREGATION_DATE_YESTERDAY
python3 add_upload_list_to_config.py final_products_datestrings_loaded.json config.json
python3 add_auth_info_to_config.py config.json

echo "[task.sh] [8/8] Attempting to upload the final files."
python3 upload.py


echo "[task.sh] All done!"
