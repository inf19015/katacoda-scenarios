#!/bin/bash
docker-compose up -d
echo "inserting data into database...."
cd ./data_creation && python ./fill_db.py
