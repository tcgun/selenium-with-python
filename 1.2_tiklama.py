from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# WebDriver'ı başlatma
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Google'a gidip pencereyi maksimize etme
driver.get("http://google.com")
driver.maximize_window()

# Arama kutusunu bulma ve "selenium" yazma
aramaKutusu = driver.find_element(By.NAME, "q")
sleep(2)
aramaKutusu.send_keys("selenium")
sleep(2)

# Google'da arama yapma (btnK butonuna tıklama)
driver.find_element(By.NAME, "btnK").click()
sleep(2)

# İlk sonuca tıklama (XPath ile belirtilen öğe)
driver.find_element(By.XPATH, "//*[@id='rso']/div[2]/div[3]/div/div/div/div[1]/div/div/span/a").click()
sleep(2)

# Tarayıcıyı kapatma
driver.quit()