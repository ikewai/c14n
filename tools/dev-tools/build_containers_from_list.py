#!/bin/python3
# A script to build every container in a list, in one pass.

import sys # For accessing execution args.
import subprocess # For spinning off docker builds.
import json # For parsing the build list.
import os # For determining no-cache
from datetime import datetime # For making time-dependent tags

fin = sys.argv[1]
fin = open(fin, "rt")
container_list = json.loads(fin.read())

try:
    BUILD_NO_CACHE = str(os.environ['BUILD_NO_CACHE'])
except:
    BUILD_NO_CACHE = '0'
# For every container provided by the file, we build the container according to the key/value pairs.
# An example build would be
# `docker build -f containers/airtemp/base/Dockerfile -t ikewai/task-at-base:latest .`
# The "-f" flag indicates that the next arg is the location of the file to build from.
# The "-t" flag indicates that the next arg is the tag of the container to be built.
# Optionally, if the "BUILD_NO_CACHE" environment variable is set to 1, the --no-cache flag
#   will be used, which tells Docker not to use any cached build steps. This is useful when
#   you want to force an apt update or remote download calls (wget, curl).
# If the tag is set to "latest", the script will create an extra tag with the
#   first seven characters of the host repo's latest commit hash.
#   Example: ikewai/task-base:427cfad (is equal to) ikewai/task-base:latest,
#   when 427cfad is the most recent commit to the main branch of the build repo.
for c in container_list:
    # if c['tag'] contains "%", replace all instances of %y, %m, %d with their respective values.
    #   This is for creating a tag that contains the date of the build, in addition to the repo hash.
    #   Example: task-base:%y-%m-%d-*hash -> task-base:2023-03-14-b2061a1
    if "%" in c['tag']:
        # Get the date
        now = datetime.now()
        current_year = str(now.year)
        current_month = str(now.month)
        if current_month < 10:
            current_month = "0" + current_month
        current_day = str(now.day)
        if current_day < 10:
            current_day = "0" + current_day

        # Replace the %y, %m, %d with the date
        tag = c['tag'].replace("%y", current_year)
        tag = tag.replace("%m", current_month)
        tag = tag.replace("%d", current_day)

        # Get the repo hash
        repo_hash = subprocess.run(["/bin/bash", "-c", "git rev-parse --short HEAD"], capture_output=True).stdout.decode().strip("\n")
        tag = tag.replace("*hash", repo_hash)

        # Build the container
        cmd = f"docker build \
        {'--no-cache' if BUILD_NO_CACHE=='1' else ''} \
        -f {c['rel_location']}/Dockerfile \
        -t {c['image_name']}:{tag} ."

        print(f"Running command: {cmd}")
        subprocess.run(["/bin/bash", "-c", cmd])
    else:
        # Build the container exactly as specified.
        cmd = f"docker build \
        {'--no-cache' if BUILD_NO_CACHE=='1' else ''} \
        -f {c['rel_location']}/Dockerfile \
        -t {c['image_name']}:{c['tag']} ."

        print(f"Running command: {cmd}")
        subprocess.run(["/bin/bash", "-c", cmd])

