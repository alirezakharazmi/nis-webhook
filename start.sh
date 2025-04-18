#!/bin/bash

# دانلود و نصب گوگل کروم
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
apt-get install -y ./google-chrome-stable_current_amd64.deb

# تنظیم مسیر chrome برای Selenium
export CHROME_BIN=/usr/bin/google-chrome

# اجرای اپ با Gunicorn
gunicorn app:app --bind 0.0.0.0:$PORT
