#!/bin/python3

import sys, subprocess

fin = open(sys.argv[1], "rt")

for line in fin:
    subprocess.run(["mkdir", "-p", f"{str(line).strip()}"])