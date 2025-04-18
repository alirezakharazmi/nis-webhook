#!/bin/bash

# مسیر مقصد برای کروم و کروم‌درایور
CHROME_DIR=$PWD/chrome

# اگر فولدر chrome وجود نداره بساز
mkdir -p $CHROME_DIR

# دانلود و استخراج Google Chrome
wget -q -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
ar x chrome.deb
tar -xvf data.tar.xz --directory=$CHROME_DIR ./opt/google/chrome/google-chrome

# دانلود و استخراج ChromeDriver
wget -q -O chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/linux64/chromedriver-linux64.zip
unzip -q chromedriver.zip -d $CHROME_DIR
mv $CHROME_DIR/chromedriver-linux64/chromedriver $CHROME_DIR/

# مجوز اجرا بده
chmod +x $CHROME_DIR/google-chrome
chmod +x $CHROME_DIR/chromedriver

# تنظیم متغیرها
export CHROME_BIN=$CHROME_DIR/google-chrome
export PATH=$CHROME_DIR:$PATH

# اجرای اپ با گانیکورن
gunicorn app:app --bind 0.0.0.0:$PORT
