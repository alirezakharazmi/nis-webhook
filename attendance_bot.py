import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def run_attendance():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.implicitly_wait(10)

        # TODO: ورود و پر کردن فرم حضور در اینجا اضافه خواهد شد

        time.sleep(2)
        driver.save_screenshot("screenshot.png")
        driver.quit()

        # ارسال اسکرین‌شات به تلگرام
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")

        if token and chat_id:
            url = f"https://api.telegram.org/bot{token}/sendPhoto"
            with open("screenshot.png", "rb") as img:
                requests.post(url, data={"chat_id": chat_id}, files={"photo": img})

    except Exception as e:
        print(f"Error: {e}")
