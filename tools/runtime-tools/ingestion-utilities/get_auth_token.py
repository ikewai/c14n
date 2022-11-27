#!/bin/python3
# Uses Username/Password/Key/Secret Authentication to generate a short-lived token.

import os # For getting environment variables.
import sys # For getting execution arguments.
import json # For reading server responses.
import subprocess # For setting the token's env variable via bash export.

output_file = sys.argv[1]
fout = open(output_file, "wt")

# Make request to Agave (tapis v2) API server.
# This is using a raw cURL request because, for this particular use, agavepy and requests are **cursed**.
api_endpoint = "https://agaveauth.its.hawaii.edu/token"
cmd = f"curl -sku '{os.environ['IW_API_KEY']}:{os.environ['IW_API_SECRET']}' -d grant_type=password -d username={os.environ['IW_USERNAME']} -d password={os.environ['IW_PASSWORD']} -d scope=PRODUCTION {api_endpoint}"
res = subprocess.run(["/bin/bash", "-c", cmd], capture_output=True)

# Get token from response.
full_token = json.loads(res.stdout.decode())
access_token = full_token['access_token']

# Write token to file.
fout.write(access_token)
fout.close()