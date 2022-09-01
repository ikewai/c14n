#!/bin/python3
# This script injects configuration data from JSON-formatted strings
# in the environment into the "data" field of the given config file.

import os # For accessing environment variables.
import sys # For accessing execution args.
from io import TextIOWrapper # For hinting type in file read/writes.
import json # For interacting with JSON data.