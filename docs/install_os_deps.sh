#!/bin/bash
# install on clean ubuntu 12.04.4 LTS, run as root.
echo "Installing OS dependencies..."
apt-get install build-essential python-dev postgresql libpq-dev python-virtualenv python-setuptools
# install python dependencies of the software
echo "Installing Python dependencies..."
pip install -r dependencies.txt
echo "Creating database dependencies..."
sudo -u postgres psql --command '\password postgres'
echo "Creating database segue..."
sudo -u postgres psql --command 'create database segue;'
echo "Done."

