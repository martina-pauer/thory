#!/usr/bin/bash
# Install needed devs-libs for debian based linux distros
sudo -k apt-get install libgtkmm-3.0-dev
# Compile
g++ ./src/thory.cpp -o thory `pkg-config --cflags --libs gtkmm-3.0` 