#!/bin/bash
docker-compose up -d
echo "inserting data into database...."
pip install -r ./requirements.txt
python ./fill_db.py
