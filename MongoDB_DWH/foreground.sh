#!/bin/bash
docker-compose up -d
apt-get update
apt-get install python3.8-venv -y
python -m venv ./venv
source ./venv/bin/acivate
pip install -r ./requirements.txt
echo "inserting data into database...."
python ./fill_db.py
