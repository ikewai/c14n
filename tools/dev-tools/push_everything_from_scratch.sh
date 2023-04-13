#!/bin/bash

export BUILD_NO_CACHE=1

python3 push_containers_from_list.py ./container-lists/all_latest.json
python3 push_containers_from_list.py ./container-lists/all_detailed.json