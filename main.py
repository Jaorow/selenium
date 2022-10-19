from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import pathlib
from selenium.webdriver.common.by import By



path = (pathlib.Path(__file__).parent.resolve())

ser = Service(str(path)+"/chromedriver")
driver = webdriver.Chrome(service = ser)

driver.get('https://github.com/Jaorow')

data = driver.find_element(By.XPATH, '//*[@id="js-contribution-activity"]/div[2]/div/div[2]/div[2]/details/div/ul/li[1]/time')
print(data)
# time.sleep(2)