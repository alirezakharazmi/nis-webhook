from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def run_attendance_bot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = os.getenv("CHROME_BIN")

    service = Service(executable_path="chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # ادامه فرم و اسکرین‌شات...
