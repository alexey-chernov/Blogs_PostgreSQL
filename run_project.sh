#!/bin/bash

python3 -m venv virtualenv
source virtualenv/bin/activate
FLASK_APP=blog flask run -h 0.0.0.0 -p 5050
