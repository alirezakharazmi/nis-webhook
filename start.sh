#!/bin/bash

# دانلود گوگل کروم و بررسی موفقیت دانلود
echo "Downloading Chrome..."
curl -sSL -o chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

if [ ! -f chrome.deb ]; then
    echo "Download failed!"
    exit 1
fi

# استخراج در مسیر محلی
mkdir -p chrome
dpkg-deb -xv chrome.deb chrome/

# تنظیم مسیر chrome
export CHROME_BIN=$(pwd)/chrome/opt/google/chrome/google-chrome
echo "CHROME_BIN set to $CHROME_BIN"

# اجرای اپلیکیشن
gunicorn app:app --bind 0.0.0.0:$PORT
