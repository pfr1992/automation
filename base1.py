from seleniumbase import Driver

DIR ='/home/paulofernando1992/chromedata'
driver = Driver(uc=True, headless=False, user-data-dir=DIR)
#user-data-dir='/home/paulofernando1992/chromedata'
#driver.get("https://canal360i.cloud.itau.com.br/login/iparceiros")
driver.get("chrome://version/")
driver.save_screenshot("valeuveiogarcon2.png")
driver.close()
