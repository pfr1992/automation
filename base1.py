from seleniumbase import Driver

driver = Driver(uc=True)
#driver.get("https://canal360i.cloud.itau.com.br/login/iparceiros")
driver.get("chrome://version/")
driver.save_screenshot("valeuveiogarcon.png")
driver.close()
