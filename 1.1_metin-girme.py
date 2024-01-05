from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com/")
aramaKutusu = driver.find_element(By.ID, "APjFqb")
aramaKutusu.send_keys("selenium")
sleep(2)
aramaKutusu.send_keys(Keys.ENTER)
sleep(2)

driver.quit()