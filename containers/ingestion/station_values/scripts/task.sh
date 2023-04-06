#!/bin/bash
echo "[task.sh] Starting Execution."
cd /home/hcdp_tapis_ingestor/station_values

echo "[task.sh] [1/6] Downloading ingestion config."
wget $INGESTION_CONFIG_URL -O config.json

echo "[task.sh] [2/6] Updating date strings in config if requested."
if [ $UPDATE_DATES_IN_CONFIG ];
then
    if [ $CUSTOM_DATE ];
    then
        mv config.json config_temp.json
        python3 /actor/update_date_string_in_config.py \
        config_temp.json \
        config.json \
        $CUSTOM_DATE
    else
        mv config.json config_temp.json
        python3 /actor/update_date_string_in_config.py \
        config_temp.json \
        config.json
        $(date --date="last month" +%Y-%M-%d)
    fi
fi

echo "[task.sh] [3/6] Pulling files to ingest."
python3 /actor/pull_files_to_ingest.py /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [4/6] Getting and setting authentication token."
python3 /actor/get_auth_token.py IW_TOKEN.txt

echo "[task.sh] [5/6] Injecting authentication into config."
python3 /actor/inject_auth.py IW_TOKEN.txt /home/hcdp_tapis_ingestor/station_values/config.json

echo "[task.sh] [6/6] Ingesting station values."
python3 /home/hcdp_tapis_ingestor/station_values/driver.py config.json

echo "[task.sh] All done!"