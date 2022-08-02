#!/bin/bash
echo "[task.sh] Starting Execution."

echo "[task.sh] Collecting Climate data from MADIS on the daily timeframe."
cd /home/hawaii_climate_products_container/preliminary/data_aqs/code/nws_rr5
Rscript nws_rr5_hrly_24hr_webscape.R

echo "[task.sh] Injecting authentication variables for uploader."
cd /sync
python3 upload_auth_injector.py config.json

echo "[task.sh] Attempting to upload the gathered data."
python3 upload.py

echo "[task.sh] All done!