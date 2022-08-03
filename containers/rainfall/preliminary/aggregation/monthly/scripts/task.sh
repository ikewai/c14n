#!/bin/bash
echo "[task.sh] Starting Execution."

echo "[task.sh] Aggregating Rainfall data on the monthly timeframe."
cd /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/daily_to_monthly_agg_FINAL.R
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/monthly/monthly_rf_krig_map_makr_FINAL.R


echo "[task.sh] [disabled] Preparing for upload."
cd /sync
#python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
#python3 upload_list_inserter.py upload_config_datestrings_loaded.json config.json
#python3 upload_auth_injector.py config.json

echo "[task.sh] [disabled] Attempting to upload the aggregated data."
#python3 upload.py

echo "[task.sh] All done!"