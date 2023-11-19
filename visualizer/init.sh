#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_dev.txt
nodeenv --npm=8.12.1 --node=18.4.0 env 
deactivate