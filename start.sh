
#!/bin/bash

mkdir -p chrome

# دانلود Google Chrome بدون استفاده از dpkg و نصب مستقیم باینری
wget -q -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
ar x chrome.deb
tar -xf data.tar.xz --directory=chrome

# دانلود Chromedriver (نسخه 122 که با Chrome همخوانی دارد)
wget -q -O chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.111/linux64/chromedriver-linux64.zip
unzip -q chromedriver.zip -d chrome

# تنظیم دسترسی اجرایی به کروم و درایور
chmod +x chrome/opt/google/chrome/google-chrome
chmod +x chrome/chromedriver-linux64/chromedriver

# تعریف متغیرها برای استفاده در Selenium
export CHROME_BIN=$PWD/chrome/opt/google/chrome/google-chrome
export PATH=$PWD/chrome/chromedriver-linux64:$PATH

# اجرای اپ
gunicorn app:app --bind 0.0.0.0:$PORT
