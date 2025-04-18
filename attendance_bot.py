from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def run_attendance_bot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/opt/render/project/src/chrome/opt/google/chrome/google-chrome"

    service = Service("/opt/render/project/src/chrome/chromedriver-linux64/chromedriver")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    # باقی کدهای bot
    print("Attendance triggered")
    driver.quit()
