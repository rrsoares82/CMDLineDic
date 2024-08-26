#!/bin/sh
echo "Check python3 installed"
python3 --version

root_path=$(dirname $(dirname $0))

echo "Installing requirements"
python3 -m pip install -r "$root_path/requirements.txt" --break-system-packages

