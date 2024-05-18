# run both scripts
#!/bin/bash

# Check if python3 is installed
if command -v python3 &> /dev/null
then
    python3 txt-to-json.py
    python3 json-to-email.py
elif command -v python &> /dev/null
then
    python3 txt-to-json.py
    python3 json-to-email.py
else
    echo "Error: Python is not installed."
    exit 1
fi

