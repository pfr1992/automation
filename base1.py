from seleniumbase import Driver

DIR ='/home/paulofernando1992/chromedata'
driver = Driver(uc=True, headless=False, headed=True)
#user_data_dir='/home/paulofernando1992/chromedata'
#driver.get("https://canal360i.cloud.itau.com.br/login/iparceiros")
driver.get("chrome://version/")
driver.save_screenshot("valeuveiogarcon2.png")
driver.close()
