import os
import time
import requests
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

def run_attendance_bot():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
    login_url = "https://pdks.nisantasi.edu.tr"

    # تنظیمات مرورگر
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = os.getenv("CHROME_BIN")

    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(login_url)
        time.sleep(2)

        # ورود به سیستم
        driver.find_element(By.NAME, "userName").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.ID, "btnLogin").click()
        time.sleep(3)

        # ورود به بخش حضور و غیاب
        driver.get("https://pdks.nisantasi.edu.tr/lecturer/attendances")
        time.sleep(2)

        # انتخاب درس
        select_course = Select(driver.find_element(By.ID, "Course"))
        select_course.select_by_index(1)  # درس اول، می‌تونی بر اساس عنوان هم انتخاب کنی

        # انتخاب ساعت با توجه به ساعت فعلی
        now = datetime.now().strftime("%H:%M")
        select_hour = Select(driver.find_element(By.ID, "Hour"))
        options = [option.text for option in select_hour.options]
        if now in options:
            select_hour.select_by_visible_text(now)
        else:
            select_hour.select_by_index(0)  # fallback به گزینه اول

        # ارسال حضور و غیاب
        driver.find_element(By.ID, "btnSubmit").click()
        time.sleep(2)

        # گرفتن اسکرین‌شات
        screenshot_path = "screenshot.png"
        driver.save_screenshot(screenshot_path)

        # ارسال به تلگرام
        with open(screenshot_path, "rb") as photo:
            requests.post(
                f"https://api.telegram.org/bot{telegram_token}/sendPhoto",
                data={"chat_id": telegram_chat_id},
                files={"photo": photo}
            )

    except Exception as e:
        print("Error:", e)
        requests.post(
            f"https://api.telegram.org/bot{telegram_token}/sendMessage",
            data={"chat_id": telegram_chat_id, "text": f"خطا در اجرای ربات: {e}"}
        )

    finally:
        driver.quit()
