FROM ikewai/task-base

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update
# Let APT know that we don't have a terminal.
ENV DEBIAN_FRONTEND=noninteractive

# Install libgdal.
RUN apt install -y libgdal-dev

# Install R.
RUN apt install -y r-base

# Install miniconda, a lightweight form of Anaconda.
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN /bin/bash 'Miniconda3-latest-Linux-x86_64.sh -b'


# Install dependencies for the rainfall workflows.
# Specific explanations of each library coming soon.
# Libraries are approximately ordered by dependency,
# then by time-to-install.
RUN apt install -y libxml2-dev
RUN apt install -y libssl-dev
RUN apt install -y curl
RUN apt install -y libcurl4-openssl-dev
#RUN R -e 'install.packages("ggplot2")'
RUN conda install -c r r-ggplot2
#RUN R -e 'install.packages("xts")'
RUN conda install -c r r-xts
#RUN R -e 'install.packages("metScanR")'
RUN conda install -c r r-metScanR
#RUN R -e 'install.packages("lubridate")'
RUN conda install -c r r-lubridate
#RUN R -e 'install.packages("plyr")'
RUN conda install -c r r-plyr
#RUN R -e 'install.packages("reshape2")'
RUN conda install -c r r-reshape2
#RUN R -e 'install.packages("raster")'
RUN conda install -c r r-raster
#RUN R -e 'install.packages("sp")'
RUN conda install -c r r-sp
#RUN R -e 'install.packages("doParallel")'
RUN conda install -c r r-doParallel
#RUN R -e 'install.packages("foreach")'
RUN conda install -c r r-foreach
#RUN R -e 'install.packages("fitdistrplus")'
RUN conda install -c r r-fitdistrplus
#RUN R -e 'install.packages("tidyr")'
RUN conda install -c r r-tidyr
#RUN R -e 'install.packages("e1071")'
RUN conda install -c r r-e1071
#RUN R -e 'install.packages("Metrics")'
RUN conda install -c r r-Metrics
#RUN R -e 'install.packages("rgdal")'
RUN conda install -c r r-rgdal
#RUN R -e 'install.packages("geosphere")'
RUN conda install -c r r-geosphere
#RUN R -e 'install.packages("data.table")'
RUN conda install -c r r-data.table
#RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/Archive/randomForest/randomForest_4.6-14.tar.gz", repos=NULL, type="source")'
RUN conda install -c r r-randomForest
#RUN R -e 'install.packages("caret")'
RUN conda install -c r r-caret
#RUN R -e 'install.packages("dplyr")'
RUN conda install -c r r-dplyr
#RUN R -e 'install.packages("matrixStats")'
RUN conda install -c r r-matrixStats
#RUN R -e 'install.packages("automap")'
RUN conda install -c r r-automap
#RUN R -e 'install.packages("gstat")'
RUN conda install -c r r-gstat
#RUN R -e 'install.packages("svMisc")'
RUN conda install -c r r-svMisc
#RUN R -e 'install.packages("rgeos")'
RUN conda install -c r r-rgeos
#RUN R -e 'install.packages("colorRamps")'
RUN conda install -c r r-colorRamps

# Include a build script for making directories from a text file,
# in the format provided by the rainfall source code.
ADD /tools/build-tools/rainfall-specific/mkdir_from_txt.py /build/mkdir_from_txt.py

# Include a build script for downloading files specified
# in a JSON document.
ADD /tools/build-tools/wget_from_json.py /build/wget_from_json.py

## OPERATIONS ##
# Create the build's manifest.
ADD /containers/rainfall/preliminary/base/repos.json /build/repos.json
RUN python3 /tools/tagging-tools/make_build_manifest.py /build/repos.json /build/manifest.json