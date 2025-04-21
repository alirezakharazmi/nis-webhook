#!/bin/bash

mkdir -p chrome

wget -q -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
ar x chrome.deb
tar -xf data.tar.xz --directory=chrome ./opt/google/chrome

wget -q -O chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/linux64/chromedriver-linux64.zip
unzip -q chromedriver.zip -d chrome

chmod +x chrome/opt/google/chrome/google-chrome
chmod +x chrome/chromedriver-linux64/chromedriver

export CHROME_BIN=$PWD/chrome/opt/google/chrome/google-chrome
export PATH=$PWD/chrome/chromedriver-linux64:$PATH

gunicorn app:app --bind 0.0.0.0:$PORT
