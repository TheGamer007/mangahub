#!/usr/bin/env bash

chmod +x ./main.py

sudo add-apt-repository ppa:kivy-team/kivy
sudo apt-get update

sudo apt-get install python-kivy

pip install --upgrade kivy kivy-garden

garden install --app --upgrade filebrowser
