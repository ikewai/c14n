FROM ikewai/task-base

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update
# Let APT know that we don't have a terminal.
ENV DEBIAN_FRONTEND=noninteractive

# Install libgdal.
# This is experimental - The scripts had some
# issues with newer versions of gdal during previous c14n.
RUN apt install -y libgdal-dev

# Install R.
RUN apt install -y r-base

# Install dependencies for the rainfall workflows.
# Specific explanations of each library coming soon.
# Libraries are approximately ordered by dependency,
# then by time-to-install.
RUN apt install -y libxml2-dev
RUN apt install -y libssl-dev
RUN apt install -y curl
RUN apt install -y libcurl4-openssl-dev
RUN R -e 'install.packages("ggplot2")'
RUN R -e 'install.packages("xts")'
RUN R -e 'install.packages("metScanR")'
RUN R -e 'install.packages("lubridate")'
RUN R -e 'install.packages("plyr")'
RUN R -e 'install.packages("reshape2")'
RUN R -e 'install.packages("raster")'
RUN R -e 'install.packages("sp")'
RUN R -e 'install.packages("doParallel")'
RUN R -e 'install.packages("foreach")'
RUN R -e 'install.packages("fitdistrplus")'
RUN R -e 'install.packages("tidyr")'
RUN R -e 'install.packages("e1071")'
RUN R -e 'install.packages("Metrics")'
RUN R -e 'install.packages("rgdal")'
RUN R -e 'install.packages("geosphere")'
RUN R -e 'install.packages("data.table")'
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/Archive/randomForest/randomForest_4.6-14.tar.gz", repos=NULL, type="source")'
RUN R -e 'install.packages("caret")'
RUN R -e 'install.packages("dplyr")'
RUN R -e 'install.packages("matrixStats")'

# Include a build script for making directories from a text file,
# in the format provided by the rainfall source code.
ADD /tools/build-tools/rainfall-specific/mkdir_from_txt.py /build/mkdir_from_txt.py
# TODO get dir list, apply mkdir script


## OPERATIONS ##
# Create the build's manifest.
ADD /containers/rainfall/preliminary/base/repos.json /build/repos.json
RUN python3 /tools/tagging-tools/make_build_manifest.py /build/repos.json /build/manifest.json