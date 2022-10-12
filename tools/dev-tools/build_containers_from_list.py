#!/bin/python3
# A script to build every container in a list, in one pass.

import sys # For accessing execution args.
import subprocess # For spinning off docker builds.
import json # For parsing the build list.

fin = sys.argv[1]
fin = open(fin, "rt")
container_list = json.loads(fin.read())

for c in container_list:
    cmd = f"docker build \
            -f {c['rel_location']}/Dockerfile \
            -t {c['image_name']}:{c['tag']} ."
    subprocess.run(["/bin/bash", "-c", cmd])