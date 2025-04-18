#!/bin/bash

# نصب گوگل کروم
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt-get update
apt-get install -y ./google-chrome-stable_current_amd64.deb

# تنظیم مسیر کروم برای selenium
export CHROME_BIN=/usr/bin/google-chrome

# اجرای برنامه
gunicorn app:app --bind 0.0.0.0:$PORT
