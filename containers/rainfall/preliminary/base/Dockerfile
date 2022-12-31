FROM ikewai/task-base

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update
# Let APT know that we don't have a terminal.
ENV DEBIAN_FRONTEND=noninteractive

# Install OS dependencies for the rainfall workflows.
RUN apt install -y libxml2-dev
RUN apt install -y libssl-dev
RUN apt install -y curl libcurl4-openssl-dev
RUN apt install -y libgdal-dev gdal-bin
RUN apt install -y libxtst-dev libxt6 libxrender1
RUN apt install -y libudunits2-dev
RUN apt install -y r-base
### R needs to be version 4.1 or above!! need to figure this out

RUN R -e 'install.packages("jetpack", repos="http://cran.us.r-project.org")'

WORKDIR /home/hawaii_climate_products_container

RUN R -e 'jetpack::init()'

RUN R -e 'jetpack::add("proj")'
RUN R -e 'jetpack::add("sp@1.5-0")'
# `sp@1.5-1`: R >= 3.0.0
RUN R -e 'jetpack::add("geosphere@1.5-14")'
# `geosphere@1.5-18`: R >= 3.0.0
RUN R -e 'jetpack::add("spatial@7.3-15")'
# `spatial@7.3-15`: R >= 3.0.0
RUN R -e 'jetpack::add("sf@1.0-9")'
# `sf@1.0-9`: R >= 3.3.0
RUN R -e 'jetpack::add("raster@3.5-15")'
# `raster@3.6-11`: R >= 3.5.0; sp >=1.4-5
RUN R -e 'jetpack::add("ggplot2@3.4-0")'
# `ggplot2@3.4-0`: R >= 3.3.0
RUN R -e 'jetpack::add("zoo@1.8-10")'
# `zoo@1.8-11`: R >= 3.1.0
RUN R -e 'jetpack::add("xts@0.12-1")'
# `xts@0.12-2`: zoo >= 1.7-12
RUN R -e 'jetpack::add("leaflet@2.1-1")'
# `leaflet@2.1-1`: R >= 3.1.0
RUN R -e 'jetpack::add("matlab@1.0-4")'
# `matlab@1.0-4`: R >= 2.1.5
RUN R -e 'jetpack::add("RCurl@1.98-1.9")'
# `RCurl@1.98-1.9`: R >= 3.4.0
RUN R -e 'jetpack::add("foreach@1.5-2")'
# `foreach@1.5-2`: R >= 2.5.0
RUN R -e 'jetpack::add("iterators@1.0-14")'
# `iterators@1.0-14`: R >= 2.5.0
RUN R -e 'jetpack::add("doParallel@1.0-17")'
# `doParallel@1.0-17`: R >= 2.14.0; foreach >= 1.2.0; iterators >= 1.0.0
RUN R -e 'jetpack::add("MASS@7.3.55")'
# `MASS@7.3-58.1`: R >= 3.3.0
RUN R -e 'jetpack::add("survival@3.2.13")'
# `survival@3.4.0`: R >= 3.5.0
RUN R -e 'jetpack::add("fitdistrplus@1.1.8")'
# `fitdistrplus@1.1-8`: R >= 3.5.0; MASS >= 7.3-58.1; survival >= 3.4-0
RUN R -e 'jetpack::add("tidyr@1.2.1")'
# `tidyr@1.2.1`: R >= 3.1.0
RUN R -e 'jetpack::add("e1071@1.7.12")'
# `e1071@1.7-12`: none
RUN R -e 'jetpack::add("Metrics@0.1.4")'
# `Metrics@0.1-4`: none
RUN R -e 'jetpack::add("data.table@1.14.2")'
# `data.table@1.14-6`: R >= 3.1.0
RUN R -e 'jetpack::add("randomForest@4.7.1.1")'
# `randomForest@4.6-14`: R >= 3.2.2
RUN R -e 'jetpack::add("lattice@0.20-45")'
# `lattice@0.20-45`: R >= 3.0.0
RUN R -e 'jetpack::add("caret@6.0-93")'
# `caret@6.0-93`: R >= 3.2.0; ggplot2 >= 3.4-0; lattice >= 0.20
RUN R -e 'jetpack::add("dplyr@1.0.9")'
# `dplyr@1.0-8`: R >= 3.4.0
RUN R -e 'jetpack::add("matrixStats@0.62.0")'
# `matrixStats@0.63-0`: R >= 2.12.0
RUN R -e 'jetpack::add("svMisc@1.2.3")'
# `svMisc@1.2-3`: R >= 2.13.0
RUN R -e 'jetpack::add("colorRamps@2.3.1")'
# `colorRamps@2.3-1`: none
RUN R -e 'jetpack::add("rgdal@1.5.32")'
# `rgdal@1.6-3`: R >= 3.5.0; sp >= 1.1-0
RUN R -e 'jetpack::add("abind@1.4-5")'
# `abind@1.4-5`: R >= 1.5.0
RUN R -e 'jetpack::add("lwgeom@0.2-10")'
# `lwgeom@0.2-10`: R >= 3.3.0
RUN R -e 'jetpack::add("sftime@0.2-0")'
# `sftime@0.2-0`: sf >= 1.0.7
RUN R -e 'jetpack::add("stars@0.6-0")'
# `stars@0.6-0`: R >= 3.3.0; abind >= 1.4-5; sf >= 1.0-9
RUN R -e 'jetpack::add("intervals@0.15-2")'
# `intervals@0.15-2`: R >= 2.9.0
RUN R -e 'jetpack::add("spacetime@1.2-8")'
# `spacetime@1.2-8`: R >= 3.0.0
RUN R -e 'jetpack::add("FNN@1.1.3.1")'
# `FNN@1.1.3.1`: R >= 3.0.0
RUN R -e 'jetpack::add("gstat@2.1-0")'
# `gstat@2.1-0`: R >= 2.10.0
RUN R -e 'jetpack::add("reshape@0.8.9")'
# `reshape@0.8.9`: R >= 2.6.1
RUN R -e 'jetpack::add("maptools@1.1-6")'
# `maptools@1.1-6`: R >= 2.10.0; sp >= 1.0-11
RUN R -e 'jetpack::add("automap@1.0-16")'
# `automap@1.0-16`: R >= 2.10.0; sp >= 0.9-55
RUN R -e 'jetpack::add("metScanR@1.2-3")'
# `metScanR@1.2-3`: R >= 3.3.0; Note: this package is only accessible via archive.
RUN R -e 'jetpack::add("rgeos@0.6-1")'
# `rgeos@0.6-1`: R >= 3.3.0; sp >= 1.1-0

# Include a build script for making directories from a text file,
# in the format provided by the rainfall source code.
ADD /tools/build-tools/rainfall-specific/mkdir_from_txt.py /build/mkdir_from_txt.py

# Include a build script for downloading files specified
# in a JSON document.
ADD /tools/build-tools/wget_from_json.py /build/wget_from_json.py