#!/bin/bash

# Ensure the script exits on any error
set -e

# Run pytest with specified options
pytest -s -v testCases/Test_Login.py
