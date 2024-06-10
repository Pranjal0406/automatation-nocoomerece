#!/bin/bash

# Ensure the script exits on any error
set -e

# Navigate to the directory containing your tests (adjust as necessary)
cd /Users/pranjalnama/PycharmProjects/nopcommereApp

# Run pytest with specified options
pytest -s -v testCases/Test_Login.py
