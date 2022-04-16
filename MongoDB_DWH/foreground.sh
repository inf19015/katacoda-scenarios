#!/bin/bash
docker-compose up -d
echo "inserting data into database...."
python ./fill_db.py
