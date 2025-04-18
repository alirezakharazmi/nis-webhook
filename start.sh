#!/bin/bash

# دانلود و استخراج گوگل کروم در مسیر مجاز
mkdir -p chrome
curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb
dpkg-deb -xv chrome.deb chrome/
export CHROME_BIN=$(pwd)/chrome/opt/google/chrome/google-chrome

# اجرای برنامه
gunicorn app:app --bind 0.0.0.0:$PORT
