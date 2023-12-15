from seleniumbase import Driver
from seleniumbase.config import settings
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-application-cache")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-zoom=25")
options.add_argument("--disable-popup-blocking")
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--no-first-run")
options.add_argument("--no-service-autorun")
options.add_argument("--password-store=basic")

DIR = "/home/paulofernando1992/chromedata"

settings.USER_DATA_DIR = DIR

driver = Driver(uc=True, headless=False, user_data_dir=DIR, chrome_options=options)
driver.get("chrome://version/")
driver.save_screenshot("valeuveiogarcon2.png")
driver.close()
