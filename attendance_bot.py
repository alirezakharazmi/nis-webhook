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

        # وارد سایت شو
        driver.get("https://pdks.nisantasi.edu.tr/")

        # وارد کردن نام کاربری و رمز عبور
        driver.find_element(By.NAME, "username").send_keys(os.getenv("USERNAME"))
        driver.find_element(By.NAME, "password").send_keys(os.getenv("PASSWORD"))
        driver.find_element(By.TAG_NAME, "button").click()

        time.sleep(2)

        # انتخاب فیلدها و پر کردن فرم (بر اساس ساختار سایت)
        driver.find_element(By.ID, "derslik").send_keys(os.getenv("CLASSROOM"))
        driver.find_element(By.ID, "dersyeri").send_keys(os.getenv("LOCATION"))
        driver.find_element(By.ID, "ders").send_keys(os.getenv("COURSE"))
        driver.find_element(By.ID, "saat").send_keys(os.getenv("HOUR"))
        driver.find_element(By.XPATH, "//button[contains(text(),'YOKLAMAYI OLUŞTUR')]").click()

        time.sleep(2)

        # گرفتن اسکرین‌شات
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
