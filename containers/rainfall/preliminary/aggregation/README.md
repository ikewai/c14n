## Rainfall Aggregation Containers

Contents:
* [`base`](/base): Essential libraries, scripts, and directory setup.
* [`daily`](/daily): Daily aggregation.
* [`monthly`](/monthly): Monthly aggregation **and** mapping.

----
TODO: monthly agg needs inputs:
* HCDP/rainfall/HCDP_dependencies/daily_dependencies.tar.gz
* ikewai-annotated-data/HCDP/production/rainfall/new/day/statewide/partial/station_data/2022/07
* rainfall_new_day_statewide_partial_station_data_2022_07.csv

where the month/year labels are adjusted relevantly.

when downloaded, output it on the local container side as:
`Statewide_Partial_Filled_Daily_RF_mm_2022_07.csv`
within `/home/hawaii_climate_products_container/preliminary/rainfall/(more info here)`

TODO: Add packages to the base, as determined by the monthly agg files.