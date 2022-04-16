#!/bin/bash
docker-compose up -d
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r ./requirements.txt
echo "inserting data into database...."
python3 ./fill_db.py
