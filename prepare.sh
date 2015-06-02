#!/bin/sh
flake8 *.py
pip freeze > requirements.txt
