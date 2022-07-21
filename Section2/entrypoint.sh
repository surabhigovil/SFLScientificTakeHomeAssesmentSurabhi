Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@surabhigovil 
guohaolee
/
python-mysql-etl
Public
Code
Issues
Pull requests
2
Actions
Projects
Wiki
Security
Insights
python-mysql-etl/entrypoint.sh

Derek Lee inital commit
Latest commit 93102e3 on Nov 21, 2019
 History
 0 contributors
Executable File  26 lines (19 sloc)  513 Bytes

#!/bin/bash

# cd to working directory
cd /app

virtualenv="/app/.venv"
# Rebuild venv environment on startup
if [ -d "$virtualenv" ]; then
    rm -r .venv/*
fi

python3 -m venv $virtualenv
. $virtualenv/bin/activate
$virtualenv/bin/pip install -r requirements.txt

# Create tables
$virtualenv/bin/python3 /app/db.py

# Insert data values
$virtualenv/bin/python3 /app/etl.py

sleep 10

# Startup Flask to keep the container alive
# not really being used at all for now 
$virtualenv/bin/python3 /app/app.py