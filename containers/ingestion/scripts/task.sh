#!/bin/bash
echo "[task.sh] Starting Execution."

echo "[task.sh] [1/5] Pulling files to ingest."
python3 /actor/pull_files_from_env_list.py URLS_TO_GET /home/hcdp_tapis_ingestor/files/

echo "[task.sh] [2/5] Getting and setting authentication token."
python3 /actor/get_auth_token.py IW_TOKEN

echo "[task.sh] [3/5] Injecting authentication into config."
python3 /actor/inject_auth.py IW_TOKEN /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [4/5] Injecting configuration data into config."
python3 /actor/inject_conf.py DRIVER_CONF /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [5/5] Ingesting station values."
python3 /home/hcdp_tapis_injector/station_values/driver.py

echo "[task.sh] All done!"