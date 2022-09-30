#!/bin/python3
# A script to build every container in one pass.

import sys
import subprocess
import json

fin = sys.argv[1]
fin = open(fin, "rt")
container_list = json.loads(fin.read())

for c in container_list:
    cmd = f"docker build \
            -f {c['rel_location']}/Dockerfile \
            -t {c['image_name']}:{c['tag']} ."
    subprocess.run(["/bin/bash", "-c", cmd])