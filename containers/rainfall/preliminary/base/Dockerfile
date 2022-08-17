FROM ikewai/task-base

## PACKAGE/LIBRARY INSTALLATIONS ##
# Fetch the latest apt repo information.
RUN apt update
# Let APT know that we don't have a terminal.
ENV DEBIAN_FRONTEND=noninteractive

# Install libgdal.
# RUN apt install -y libgdal-dev


# Install Anaconda.
RUN wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh -O /build/Anaconda-installer.sh
RUN /bin/bash '/build/Anaconda-installer.sh' '-b'
# Add the Anaconda binaries to PATH.
ENV PATH "$PATH:/root/anaconda3/bin:/root/anaconda3/condabin"

RUN conda create -n container_env
SHELL ["/root/anaconda3/bin/conda", "run", "--no-capture-output", "-n", "container_env", "/bin/bash", "-c"]

# Update Anaconda
RUN conda update -n base -c defaults conda

# Install libmamba solver to accelerate installations
RUN conda install -n base conda-libmamba-solver
RUN conda install --experimental-solver=libmamba r-base r-essentials

# Install OS dependencies for the rainfall workflows.
RUN apt install -y libxml2-dev
RUN apt install -y libssl-dev
RUN apt install -y curl libcurl4-openssl-dev
RUN apt install -y libgdal-dev gdal-bin
RUN apt install -y libxtst-dev libxt6 libxrender1

# R dependencies for the rainfall workflows.
RUN conda install --experimental-solver=libmamba -c conda-forge proj
RUN conda install --experimental-solver=libmamba -c r r-sp
RUN conda install --experimental-solver=libmamba -c r r-geosphere
RUN conda install --experimental-solver=libmamba -c r r-raster
RUN conda install --experimental-solver=libmamba -c r r-ggplot2
RUN conda install --experimental-solver=libmamba -c r r-xts
RUN conda install --experimental-solver=libmamba -c r r-leaflet
RUN conda install --experimental-solver=libmamba -c r r-matlab
RUN conda install --experimental-solver=libmamba -c r r-rcurl
RUN conda install --experimental-solver=libmamba -c r r-doParallel
RUN conda install --experimental-solver=libmamba -c conda-forge r-fitdistrplus
RUN conda install --experimental-solver=libmamba -c r r-tidyr
RUN conda install --experimental-solver=libmamba -c r r-e1071
RUN conda install --experimental-solver=libmamba -c conda-forge r-metrics
RUN conda install --experimental-solver=libmamba -c r r-data.table
RUN conda install --experimental-solver=libmamba -c r r-randomForest
RUN conda install --experimental-solver=libmamba -c r r-caret
RUN conda install --experimental-solver=libmamba -c r r-dplyr
RUN conda install --experimental-solver=libmamba -c r r-matrixStats
RUN conda install --experimental-solver=libmamba -c r r-svMisc
RUN conda install --experimental-solver=libmamba -c r r-colorRamps
RUN conda install --experimental-solver=libmamba -c r r-rgdal

RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/spacetime_1.2-8.tar.gz", repos=NULL, type="source")'
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/FNN_1.1.3.1.tar.gz", repos=NULL, type="source")'
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/gstat_2.0-9.tar.gz", repos=NULL, type="source")'
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/automap_1.0-16.tar.gz", repos=NULL, type="source")'
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/Archive/metScanR/metScanR_1.2.3.tar.gz", repos=NULL, type="source")'
RUN R -e 'install.packages("https://cran.r-project.org/src/contrib/rgeos_0.5-9.tar.gz", repos=NULL, type="source")'

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