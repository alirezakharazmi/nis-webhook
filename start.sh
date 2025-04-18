#!/bin/bash

# دانلود و استخراج Chrome
mkdir -p chrome
cd chrome
wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.57/linux64/chrome-linux64.zip
unzip chrome-linux64.zip
cd ..

# دانلود chromedriver (همون نسخه Chrome)
mkdir -p chromedriver
cd chromedriver
wget https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.57/linux64/chromedriver-linux64.zip
unzip chromedriver-linux64.zip
cd ..

# تنظیم مسیرها برای استفاده در selenium
export CHROME_BIN=$(pwd)/chrome/chrome-linux64/chrome
export PATH=$PATH:$(pwd)/chromedriver/chromedriver-linux64

# اجرای اپلیکیشن
gunicorn app:app --bind 0.0.0.0:$PORT
