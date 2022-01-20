#!/bin/sh
python3 -m venv venv
source venv/bin/activate
pip install -r install_requirements.txt
pip install .
