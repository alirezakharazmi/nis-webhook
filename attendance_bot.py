
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def run_attendance_bot():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = os.environ.get("CHROME_BIN")

    driver = webdriver.Chrome(options=options)
    ...
