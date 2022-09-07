## Workflow Data Ingestion Container

A container for ingesting data from the science workflow as metadata for the gateway API.

The build process pulls from [`ikewai/hcdp_tapis_ingestor`](https://github.com/ikewai/hcdp_tapis_ingestor) for the driver script and example config.
Currently, it only uses the [station value](https://github.com/ikewai/hcdp_tapis_ingestor/tree/master/station_values) driver/config pair.

The [task definition script](/containers/ingestion/scripts/task.sh) performs three operations:
1. Pull an authentication token from the container's IW_TOKEN environment variable, which is provided by the host at runtime, and place it into the config file.
2. Pull the configuration info (file list, metadata, etc) from the container's DRIVER_CONF environment variable, which is provided by the host at runtime, and place it into the config file.
3. Execute the driver script.

Environment Variable Examples:
```sh
IW_TOKEN="4fd6..."
DRIVER_CONF="{\
'replace_duplicates':true,\
'data_col_start':13,\
'id_col':0,\
'nodata':'NA',\
'datatype':'temperature',\
'period':'day',\
'fill':'raw',\
'start_date':'2022-03-02',\
'end_date':'2022-03-03',\
'additional_properties':'{\"aggregation\":\"min\"}',\
'additional_key_properties':'[\"aggregation\"]',\
'files':'[\"temperature_min_day_statewide_raw_station_data_2022_03.csv\"]'\
}"
```