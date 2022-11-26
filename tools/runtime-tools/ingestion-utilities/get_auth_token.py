#!/bin/python3
# Uses Username/Password/Key/Secret Authentication to generate a short-lived token.

import os # For getting environment variables.
import sys # For getting execution arguments.
from agavepy import Agave # For communicating with the gateway.
import subprocess # For setting the token's env variable via bash export.

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
os.environ['CURL_CA_BUNDLE']="" # This is a temporary hack. It will be fixed soon.

token_env_key = sys.argv[1]

# Initialize Agave object.
ag = Agave(api_server="https://agaveauth.its.hawaii.edu",
           username=os.environ['IW_USERNAME'],
           password=os.environ['IW_PASSWORD'],
           client_name=os.environ['IW_CLIENT_NAME'],
           api_key=os.environ['IW_API_KEY'],
           api_secret=os.environ['IW_API_SECRET']
)

# Acquire tokens.

new_tokens = ag.tokens()
access_token = new_tokens['access_token']

# Set token in system's bash environment.
subprocess.run(["/bin/bash", "-c", f"export {token_env_key}={access_token}"])