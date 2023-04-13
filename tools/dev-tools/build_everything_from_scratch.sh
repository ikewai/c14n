#!/bin/bash

export BUILD_NO_CACHE=1

python3 build_containers_from_list.py ./container-lists/all_latest.json
python3 tag_latest_to_detailed.py ./container-lists/all_latest.json