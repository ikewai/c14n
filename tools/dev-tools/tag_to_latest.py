#!/bin/python3

import sys # For accessing execution args.
import subprocess # For spinning off docker tagging actions.
import json # For parsing the tag list.
from datetime import datetime # For making time-dependent tags

fin = sys.argv[1]
fin = open(fin, "rt")
container_list = json.loads(fin.read())

for c in container_list:
    # If the tag is time or hash-dependent, generate and substitute them before uploading
    if "%" in c['tag']:
        # Get the date
        now = datetime.now()
        current_year = str(now.year)
        current_month = str(now.month)
        if int(current_month) < 10:
            current_month = "0" + current_month
        current_day = str(now.day)
        if int(current_day) < 10:
            current_day = "0" + current_day

        # Replace the %y, %m, %d with the date
        tag = c['tag'].replace("%y", current_year)
        tag = tag.replace("%m", current_month)
        tag = tag.replace("%d", current_day)

        # Get the repo hash
        repo_hash = subprocess.run(["/bin/bash", "-c", "git rev-parse --short HEAD"], capture_output=True).stdout.decode().strip("\n")
        tag = tag.replace("*hash", repo_hash)
        cmd = f"docker tag {c['image_name']}:{tag} {c['image_name']}:latest"
        subprocess.run(["/bin/bash", "-c", cmd])