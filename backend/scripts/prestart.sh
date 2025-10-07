#! /usr/bin/env bash

set -e
set -x

# Let the DB start
python bookstore/backend_pre_start.py

# Create initial data in DB
python bookstore/initial_data.py
