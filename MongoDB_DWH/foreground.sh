#!/bin/bash
docker-compose -p dwh up -d
apt-get -o DPkg::Lock::Timeout=60 install python3.8-venv -y
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r ./requirements.txt
source ./venv/bin/activate
python ./fill_db.py
echo "you can now move on."
