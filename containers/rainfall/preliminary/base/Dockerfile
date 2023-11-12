FROM ghcr.io/ikewai/task-base:latest
LABEL org.opencontainers.image.source="https://github.com/ikewai/c14n"
LABEL org.opencontainers.image.description="Base Image for preliminary rainfall workflows."

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

WORKDIR /build

RUN R -e 'install.packages("sp", version="1.4-7", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `sp@1.5-1`: R >= 3.0.0
RUN R -e 'install.packages("geosphere", version="1.5-14", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `geosphere@1.5-18`: R >= 3.0.0
RUN R -e 'install.packages("spatial", version="7.3-15", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `spatial@7.3-15`: R >= 3.0.0
RUN R -e 'install.packages("sf", version="1.0-9", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `sf@1.0-9`: R >= 3.3.0
RUN R -e 'install.packages("raster", version="3.5-15", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `raster@3.6-11`: R >= 3.5.0; sp >=1.4-5
RUN R -e 'install.packages("ggplot2", version="3.3-6", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `ggplot2@3.4-0`: R >= 3.3.0
RUN R -e 'install.packages("zoo", version="1.8-10", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `zoo@1.8-11`: R >= 3.1.0
RUN R -e 'install.packages("xts", version="0.12-1", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `xts@0.12-2`: zoo >= 1.7-12
RUN R -e 'install.packages("leaflet", version="2.1-1", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `leaflet@2.1-1`: R >= 3.1.0
RUN R -e 'install.packages("matlab", version="1.0-4", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `matlab@1.0-4`: R >= 2.1.5
RUN R -e 'install.packages("RCurl", version="1.98-1.9", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `RCurl@1.98-1.9`: R >= 3.4.0
RUN R -e 'install.packages("foreach", version="1.5-2", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `foreach@1.5-2`: R >= 2.5.0
RUN R -e 'install.packages("iterators", version="1.0-14", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `iterators@1.0-14`: R >= 2.5.0
RUN R -e 'install.packages("doParallel", version="1.0-17", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `doParallel@1.0-17`: R >= 2.14.0; foreach >= 1.2.0; iterators >= 1.0.0
RUN R -e 'install.packages("MASS", version="7.3.57", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `MASS@7.3-58.1`: R >= 3.3.0
RUN R -e 'install.packages("survival", version="3.3.1", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `survival@3.4.0`: R >= 3.5.0
RUN R -e 'install.packages("fitdistrplus", version="1.1.8", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `fitdistrplus@1.1-8`: R >= 3.5.0; MASS >= 7.3-58.1; survival >= 3.4-0
RUN R -e 'install.packages("tidyr", version="1.2.1", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `tidyr@1.2.1`: R >= 3.1.0
RUN R -e 'install.packages("e1071", version="1.7.12", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `e1071@1.7-12`: none
RUN R -e 'install.packages("Metrics", version="0.1.4", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `Metrics@0.1-4`: none
RUN R -e 'install.packages("data.table", version="1.14.2", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `data.table@1.14-6`: R >= 3.1.0
RUN R -e 'install.packages("randomForest", version="4.7.1.1", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `randomForest@4.6-14`: R >= 3.2.2
RUN R -e 'install.packages("lattice", version="0.20-45", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `lattice@0.20-45`: R >= 3.0.0
RUN R -e 'install.packages("caret", version="6.0-93", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `caret@6.0-93`: R >= 3.2.0; ggplot2 >= 3.4-0; lattice >= 0.20
RUN R -e 'install.packages("dplyr", version="1.0.9", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `dplyr@1.0-8`: R >= 3.4.0
RUN R -e 'install.packages("matrixStats", version="0.62.0", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `matrixStats@0.63-0`: R >= 2.12.0
RUN R -e 'install.packages("svMisc", version="1.2.3", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `svMisc@1.2-3`: R >= 2.13.0
RUN R -e 'install.packages("colorRamps", version="2.3.1", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `colorRamps@2.3-1`: none
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/Archive/rgdal/rgdal_1.5-32.tar.gz", type="source", repos=NULL)'
# `rgdal@1.6-3`: R >= 3.5.0; sp >= 1.1-0
RUN R -e 'install.packages("abind", version="1.4-5", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `abind@1.4-5`: R >= 1.5.0
RUN R -e 'install.packages("lwgeom", version="0.2-10", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `lwgeom@0.2-10`: R >= 3.3.0
RUN R -e 'install.packages("sftime", version="0.2-0", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `sftime@0.2-0`: sf >= 1.0.7
RUN R -e 'install.packages("stars", version="0.6-0", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `stars@0.6-0`: R >= 3.3.0; abind >= 1.4-5; sf >= 1.0-9
RUN R -e 'install.packages("intervals", version="0.15-2", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `intervals@0.15-2`: R >= 2.9.0
RUN R -e 'install.packages("spacetime", version="1.2-8", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `spacetime@1.2-8`: R >= 3.0.0
RUN R -e 'install.packages("FNN", version="1.1.3.1", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `FNN@1.1.3.1`: R >= 3.0.0
RUN R -e 'install.packages("gstat", version="2.1-0", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `gstat@2.1-0`: R >= 2.10.0
RUN R -e 'install.packages("reshape", version="0.8.9", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `reshape@0.8.9`: R >= 2.6.1
RUN R -e 'install.packages("maptools", version="1.1-6", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `maptools@1.1-6`: R >= 2.10.0; sp >= 1.0-11
RUN R -e 'install.packages("automap", version="1.0-16", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `automap@1.0-16`: R >= 2.10.0; sp >= 0.9-55
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/Archive/metScanR/metScanR_1.2.3.tar.gz", type="source", repos=NULL)'
# `metScanR@1.2-3`: R >= 3.3.0; Note: this package is only accessible via archive.
RUN R -e 'install.packages("rgeos", version="0.5-9", repos="https://ftp.ussg.iu.edu/CRAN/")'
# `rgeos@0.6-1`: R >= 3.3.0; sp >= 1.1-0

# Include a build script for making directories from a text file,
# in the format provided by the rainfall source code.
ADD /tools/build-tools/rainfall-specific/mkdir_from_txt.py /build/mkdir_from_txt.py

# Include a build script for downloading files specified
# in a JSON document.
ADD /tools/build-tools/wget_from_json.py /build/wget_from_json.py