#!/bin/bash
echo "[task.sh] Starting Execution."

echo "[task.sh] Collecting Climate data from MADIS on the daily timeframe."
cd /home/hawaii_climate_products_container/preliminary/data_aqs/code/madis
python3 mesonet_24hr_fetch_dev.py
python3 hfmetar_24hr_fetch_dev.py

echo "[task.sh] Injecting authentication variables for uploader."
cd /sync
python3 upload_auth_injector.py config.json

echo "[task.sh] Attempting to upload the gathered data."
python3 upload.py

echo "[task.sh] All done!