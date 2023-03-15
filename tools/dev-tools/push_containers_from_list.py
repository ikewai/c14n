#!/bin/python3
# A script to push every container in a list, in one pass.

import sys # For accessing execution args.
import subprocess # For spinning off docker pushes.
import json # For parsing the push list.
from datetime import datetime # For making time-dependent tags

fin = sys.argv[1]
fin = open(fin, "rt")
container_list = json.loads(fin.read())

for c in container_list:
    # If the tag is time or hash-dependent, generate and substitute them before uploading
    if "%" in c['tag']:
        # Get the date
        now = datetime.now()
        current_year = now.year
        current_month = now.month
        current_day = now.day

        # Replace the %y, %m, %d with the date
        tag = c['tag'].replace("%y", str(current_year))
        tag = tag.replace("%m", str(current_month))
        tag = tag.replace("%d", str(current_day))

        # Get the repo hash
        repo_hash = subprocess.run(["/bin/bash", "-c", "git rev-parse --short HEAD"], capture_output=True).stdout.decode().strip("\n")
        tag = tag.replace("*hash", repo_hash)
    else:
        # If the tag has no time or hash dependencies, just use the tag as-is.
        cmd = f"docker push {c['image_name']}:{c['tag']}"
        subprocess.run(["/bin/bash", "-c", cmd])