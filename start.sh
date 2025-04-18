#!/bin/bash

# دانلود نسخه آماده‌ی گوگل کروم بدون نیاز به نصب
mkdir -p /opt/chrome
curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb
dpkg-deb -xv chrome.deb /opt/chrome/
export CHROME_BIN=/opt/chrome/opt/google/chrome/google-chrome

# اجرای برنامه
gunicorn app:app --bind 0.0.0.0:$PORT
