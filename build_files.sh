#!/bin/bash

# Install pipenv if not already installed
pip install pipenv

# Install dependencies
pipenv install -r requirements.txt

# Run Django collectstatic
pipenv run python3.10 manage.py collectstatic --noinput
