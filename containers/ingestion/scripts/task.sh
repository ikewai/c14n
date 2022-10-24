#!/bin/bash
echo "[task.sh] Starting Execution."
cd /home/hcdp_tapis_ingestor/station_values
echo "[task.sh] [1/8] Downloading ingestion config from $INGESTION_CONFIG_URL."
wget $INGESTION_CONFIG_URL -O config.json

echo "[task.sh] [2/8] Updating date strings in config if requested."
if [ $UPDATE_DATES_IN_CONFIG ] then
    python3 /actor/update_date_string_in_config.py config.json
fi

echo "[task.sh] [3/8] Downloading list of files to ingest from $INGESTION_FILES_LIST_URL."
wget $INGESTION_FILES_LIST_URL -O file_list.json

echo "[task.sh] [4/8] Pulling files to ingest."
python3 /actor/wget_from_json_list.py file_list.json

echo "[task.sh] [5/8] Getting and setting authentication token."
python3 /actor/get_auth_token.py IW_TOKEN

echo "[task.sh] [6/8] Injecting authentication into config."
python3 /actor/inject_auth.py IW_TOKEN /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [7/8] Injecting configuration data into config."
python3 /actor/inject_conf.py DRIVER_CONF /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [8/8] Ingesting station values."
python3 /home/hcdp_tapis_injector/station_values/driver.py

echo "[task.sh] All done!"