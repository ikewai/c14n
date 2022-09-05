#!/bin/bash
echo "[task.sh] [1/4] Starting Execution."

echo "[task.sh] [2/4] Injecting authentication into config."
python3 /actor/inject_auth.py IW_TOKEN /home/hcdp_tapis_injector/station_values/config.json

echo "[task.sh] [3/4] Injecting configuration data into config."
python3 /actor/inject_conf.py DRIVER_CONF /home/hcdp_tapis_injector/station_values/config.json

echo "[task.sh] [4/4] Ingesting station values."
python3 /home/hcdp_tapis_injector/station_values/driver.py