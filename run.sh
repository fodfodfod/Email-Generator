#!/bin/sh
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"
source "$parent_path/.venv/bin/activate"
python3 file_parser email-template.txt |  python3 email_generator