#!/bin/bash

# Ensure the script exits on any error
set -e

# Navigate to the directory containing your tests (adjust as necessary)
pip install pytest

# Run pytest with specified options
pytest -s -v testCases/Test_Login.py
