from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

def run_attendance_bot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # مسیر دقیق باینری گوگل کروم
    chrome_path = "/opt/render/project/src/chrome/opt/google/chrome/google-chrome"
    chromedriver_path = "/opt/render/project/src/chrome/chromedriver-linux64/chromedriver"

    # بررسی وجود فایل‌ها قبل از استفاده
    if not os.path.exists(chrome_path):
        raise FileNotFoundError(f"Chrome binary not found at {chrome_path}")
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"Chromedriver not found at {chromedriver_path}")

    chrome_options.binary_location = chrome_path
    service = Service(executable_path=chromedriver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("Attendance triggered")
    driver.quit()
