## Ingestion Container for Weather Station Values

A container for ingesting data from the science workflow as metadata for the gateway API.

The build process pulls from [`ikewai/hcdp_tapis_ingestor`](https://github.com/ikewai/hcdp_tapis_ingestor) for the driver script.

The [task definition script](/containers/ingestion/scripts/task.sh) performs 6 operations:
1. Download the ingestion configuration as defined by `INGESTION_CONFIG_URL` and places it into `/home/hcdp_tapis_ingestor/station_values/` as `config.json`.
2. If `UPDATE_DATES_IN_CONFIG` is set to true, replace `%y`, `%m`, `%d` in `config.json` with their respective values. TODO: Add ISO 8601 passthrough from env
3. Downloads and places the files specified in `config.json`.
4. Acquires a short-lived authentication token for the ingestor to execute with.
5. Places the authentication token into `config.json`.
6. Executes the ingestor.


Minimum Environment Example:
```sh
# URL to the ingestion config file. Do not use quotes around this.
INGESTION_CONFIG_URL=https://raw.githubusercontent.com/ikewai/airtemp/prod/ingestion/daily/tmax.json

# Whether or not the default datestring replacer (%y -> 2023) should be used. Should be 1 for production.
UPDATE_DATES_IN_CONFIG=1

# Authentication parameters. All are mandatory.
# A client can be created interactively via agavepy (v2) or tapipy (v3).
IW_USERNAME=username
IW_PASSWORD=password
IW_CLIENT_NAME=client_name
IW_API_KEY=api_key
IW_API_SECRET=api_secret
```