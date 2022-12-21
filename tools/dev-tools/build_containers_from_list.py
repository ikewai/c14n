#!/bin/python3
# A script to build every container in a list, in one pass.

import sys # For accessing execution args.
import subprocess # For spinning off docker builds.
import json # For parsing the build list.
import os # For determining no-cache

fin = sys.argv[1]
fin = open(fin, "rt")
container_list = json.loads(fin.read())

# For every container provided by the file, we build the container according to the key/value pairs.
# An example build would be
# `docker build -f containers/airtemp/base/Dockerfile -t ikewai/task-at-base:latest .`
# The "-f" flag indicates that the next arg is the location of the file to build from.
# The "-t" flag indicates that the next arg is the tag of the container to be built.
# Optionally, if the "BUILD_NO_CACHE" environment variable is set to 1, the --no-cache flag
#   will be used, which tells Docker not to use any cached build steps. This is useful when
#   you want to force an apt update or remote download calls (wget, curl).
# If the tag is set to "latest", the script will create an extra tag with the
#   first eight characters of the host repo's latest commit hash.
#   Example: ikewai/task-base:427cfadd (is equal to) ikewai/task-base:latest,
#   when 427cfadd is the most recent commit to the main branch of the build repo.
for c in container_list:
    cmd = f"docker build \
        -f {c['rel_location']}/Dockerfile \
        {'--no-cache' if os.environ['BUILD_NO_CACHE']=='1' else ''} \
        -t {c['image_name']}:{c['tag']} ."
    print(f"Running command: {cmd}")
    subprocess.run(["/bin/bash", "-c", cmd])

    if c['tag'] == "latest":
        repo_hash = subprocess.run(["/bin/bash", "-c", "tools/tagging-tools/get_hash.sh"], capture_output=True).stdout.decode()
        cmd = f"docker build \
        -f {c['rel_location']}/Dockerfile \
        {'--no-cache' if os.environ['BUILD_NO_CACHE']=='1' else ''} \
        -t {c['image_name']}:{repo_hash} ."
        print(f"Running command: {cmd}")
        subprocess.run(["/bin/bash", "-c", cmd])