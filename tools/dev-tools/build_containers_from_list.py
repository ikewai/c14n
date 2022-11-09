#!/bin/python3
# A script to build every container in a list, in one pass.

import sys # For accessing execution args.
import subprocess # For spinning off docker builds.
import json # For parsing the build list.
import os # For determining no-cache

fin = sys.argv[1]
fin = open(fin, "rt")
container_list = json.loads(fin.read())

for c in container_list:
    cmd = f"docker build \
        -f {c['rel_location']}/Dockerfile \
        {'--no-cache' if os.environ['BUILD_NO_CACHE']==1 else ''} \
        -t {c['image_name']}:{c['tag']} ."
    print(f"Running command: {cmd}")
    subprocess.run(["/bin/bash", "-c", cmd])