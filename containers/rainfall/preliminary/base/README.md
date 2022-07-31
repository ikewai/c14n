## `task-rf-pre-base`: All the programs and libraries necessary for running preliminary rainfall workflows.

Build includes:

* Base image: `ikewai/task-base`

* Programs:
    * [R](https://packages.ubuntu.com/focal/r-base) (Latest Stable on APT)

* OS Packages:
    * [libxml2-dev](https://packages.ubuntu.com/focal/libxml2-dev) (Latest Stable on APT)
    * [libssl-dev](https://packages.ubuntu.com/focal/libssl-dev)
    * [curl](https://packages.ubuntu.com/focal/curl) 
    * [libcurl4-openssl-dev](https://packages.ubuntu.com/focal/libcurl4-openssl-dev) 

* R Packages:
    * `ggplot2`
    * `xts`
    * `metScanR`
    * `lubridate`
    * `plyr`
    * `reshape2`
    * `raster`
    * `sp`
    * `doParallel`
    * `foreach`
    * `fitdistrplus`
    * `tidyr`
    * `e1071`
    * `Metrics`
    * `rgdal`
    * `geosphere`
    * `data.table`
    * `randomForest`
    * `caret`
    * `dplyr`
    * `matrixStats`
