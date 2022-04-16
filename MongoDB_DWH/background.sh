apt-get update
apt-get install python3.8-venv -y
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r ./requirements.txt
