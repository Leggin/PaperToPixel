set -a
python3 venv venv
source venv/bin/activate
pip install -r requirements.txt
nodeenv --node=21.2.0 env 
. env/bin/activate