#! /usr/bin/env bash

set -e
set -x

# Let the DB start
python book_store/backend_pre_start.py

# Create initial data in DB
python book_store/initial_data.py
