#!/bin/sh
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
python3 -m venv "$parent_path/.venv"
source "$parent_path/.venv/bin/activate"
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib