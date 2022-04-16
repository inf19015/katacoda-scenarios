#!/bin/bash
docker-compose up -d
source ./venv/bin/activate
echo "you can now move on."
python ./fill_db.py
