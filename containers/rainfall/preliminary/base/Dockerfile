FROM ikewai/task-base

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update
# Let APT know that we don't have a terminal.
ENV DEBIAN_FRONTEND=noninteractive

# Install libgdal.
# RUN apt install -y libgdal-dev


# Install miniconda, a minimal form of Anaconda.
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /build/Miniconda3-latest-Linux-x86_64.sh
RUN /bin/bash '/build/Miniconda3-latest-Linux-x86_64.sh' '-b'
RUN /root/miniconda3/bin/conda create -n container_env r-essentials r-base
SHELL ["/root/miniconda3/bin/conda", "run", "--no-capture-output", "-n", "container_env", "/bin/bash", "-c"]

# Install dependencies for the rainfall workflows.
# Specific explanations of each library coming soon.
RUN apt install -y libxml2-dev
RUN apt install -y libssl-dev
RUN apt install -y curl
RUN apt install -y libcurl4-openssl-dev
#RUN apt install -y libgdal-dev

RUN /root/miniconda3/bin/conda install -c conda-forge proj
RUN /root/miniconda3/bin/conda install -c r r-sp
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/rgdal_1.5-32.tar.gz", repos=NULL, type="source")'
RUN /root/miniconda3/bin/conda install -c r r-rgeos
RUN /root/miniconda3/bin/conda install -c r r-raster
RUN /root/miniconda3/bin/conda install -c r r-ggplot2
RUN /root/miniconda3/bin/conda install -c r r-xts
RUN /root/miniconda3/bin/conda install -c r r-geosphere
RUN /root/miniconda3/bin/conda install -c r r-leaflet
RUN /root/miniconda3/bin/conda install -c r r-matlab
RUN /root/miniconda3/bin/conda install -c r r-rcurl
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/Archive/metScanR/metScanR_1.2.3.tar.gz", repos=NULL, type="source")'
RUN /root/miniconda3/bin/conda install -c r r-lubridate
RUN /root/miniconda3/bin/conda install -c r r-plyr
RUN /root/miniconda3/bin/conda install -c r r-reshape2
RUN /root/miniconda3/bin/conda install -c r r-doParallel
RUN /root/miniconda3/bin/conda install -c r r-foreach
RUN /root/miniconda3/bin/conda install -c conda-forge r-fitdistrplus
RUN /root/miniconda3/bin/conda install -c r r-tidyr
RUN /root/miniconda3/bin/conda install -c r r-e1071
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/Metrics_0.1.4.tar.gz", repos=NULL, type="source")'
RUN /root/miniconda3/bin/conda install -c r r-data.table
RUN /root/miniconda3/bin/conda install -c r r-randomForest
RUN /root/miniconda3/bin/conda install -c r r-caret
RUN /root/miniconda3/bin/conda install -c r r-dplyr
RUN /root/miniconda3/bin/conda install -c r r-matrixStats
RUN /root/miniconda3/bin/conda install -c conda-forge r-automap
RUN /root/miniconda3/bin/conda install -c conda-forge r-gstat
RUN /root/miniconda3/bin/conda install -c r r-svMisc
RUN /root/miniconda3/bin/conda install -c r r-colorRamps

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