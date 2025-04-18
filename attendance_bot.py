import os
import time
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_current_hour_option():
    now = datetime.now()
    minute = 30 if now.minute >= 30 else 0
    hour = now.replace(minute=minute, second=0, microsecond=0)
    return hour.strftime("%H:%M")

def run_attendance():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.implicitly_wait(10)

        # ورود به سایت
        driver.get("https://pdks.nisantasi.edu.tr/")

        # وارد کردن نام کاربری و رمز عبور
        driver.find_element(By.NAME, "username").send_keys(os.getenv("USERNAME"))
        driver.find_element(By.NAME, "password").send_keys(os.getenv("PASSWORD"))
        driver.find_element(By.TAG_NAME, "button").click()

        time.sleep(2)

        # پر کردن فرم
        driver.find_element(By.ID, "derslik").send_keys(os.getenv("CLASSROOM"))
        driver.find_element(By.ID, "dersyeri").send_keys(os.getenv("LOCATION"))

        # انتخاب درس بر اساس COURSE_CODE
        course_code = os.getenv("COURSE_CODE", "")
        course_dropdown = Select(driver.find_element(By.ID, "ders"))
        for option in course_dropdown.options:
            if course_code in option.text:
                course_dropdown.select_by_visible_text(option.text)
                break

        # انتخاب ساعت براساس زمان اجرا
        saat = get_current_hour_option()
        saat_dropdown = Select(driver.find_element(By.ID, "saat"))
        for option in saat_dropdown.options:
            if saat in option.text:
                saat_dropdown.select_by_visible_text(option.text)
                break

        # کلیک روی دکمه
        driver.find_element(By.XPATH, "//button[contains(text(),'YOKLAMAYI OLUŞTUR')]").click()
        time.sleep(3)

        # گرفتن اسکرین‌شات
        driver.save_screenshot("screenshot.png")
        driver.quit()

        # ارسال به تلگرام
        token = os.getenv("TELEGRAM_BOT_TOKEN")
        chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if token and chat_id:
            url = f"https://api.telegram.org/bot{token}/sendPhoto"
            with open("screenshot.png", "rb") as img:
                requests.post(url, data={"chat_id": chat_id}, files={"photo": img})

    except Exception as e:
        print(f"Error: {e}")
