#!/bin/bash
docker-compose up -d
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r ./requirements.txt
source ./venv/bin/activate
python ./fill_db.py
echo "you can now move on."
