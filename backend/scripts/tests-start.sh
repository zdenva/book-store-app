#! /usr/bin/env bash
set -e
set -x

python bookstore/tests_pre_start.py

bash scripts/test.sh "$@"
