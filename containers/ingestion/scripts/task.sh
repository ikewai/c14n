#!/bin/bash
echo "[task.sh] Starting Execution."
cd /home/hcdp_tapis_ingestor/station_values

echo "[task.sh] [1/7] Downloading ingestion config."
wget $INGESTION_CONFIG_URL -O config.json

echo "[task.sh] [2/7] Updating date strings in config if requested."
if [ $UPDATE_DATES_IN_CONFIG ];
then
    mv config.json config_temp.json
    python3 /actor/update_date_string_in_config.py \
    config_temp.json \
    config.json
fi

echo "[task.sh] [3/7] Pulling files to ingest."
python3 /actor/pull_files_to_ingest.py /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [4/7] Getting and setting authentication token."
python3 /actor/get_auth_token.py IW_TOKEN

echo "[task.sh] [5/7] Injecting authentication into config."
python3 /actor/inject_auth.py IW_TOKEN /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [6/7] Injecting configuration data into config."
python3 /actor/inject_conf.py DRIVER_CONF /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [7/7] Ingesting station values."
python3 /home/hcdp_tapis_injector/station_values/driver.py

echo "[task.sh] All done!"