#!/bin/sh
echo "Check python3 installed"
python3 --version

root_path=$(dirname $(dirname $0))

echo "Installing pip"
apt install python3-pip -y

echo "Installing requirements"
python3 -m pip install -r "$root_path/requirements.txt" --break-system-packages

