#!/bin/bash
docker-compose up -d
source ./venv/bin/activate
python ./fill_db.py
echo "you can now move on."
