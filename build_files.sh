#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run Django collectstatic
python3 manage.py collectstatic --noinput
