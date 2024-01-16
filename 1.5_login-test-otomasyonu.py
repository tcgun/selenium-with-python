from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("mauro")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
sleep(2)
message = driver.find_element(By.ID, "flash").text

if "Your username is invalid!" in message:
    print("OK: Yanlış kullanıcı adı doğru çalışıyor. ")
else:
    print("HATA: Yanlış kullanıcı adı çalışmıyor.")

driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("icardi")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
sleep(2)
message2 = driver.find_element(By.ID, "flash").text

if "Your password is invalid!" in message2:
    print("OK: Yanlış şifre doğru çalışıyor. ")
else:
    print("HATA: Yanlış şifre çalışmıyor.")


driver.get("https://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()
sleep(2)
message3 = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message3:
    print("OK: Bilgiler doğru. ")
else:
    print("HATA: Bilgiler yanlış.")

sleep(2)

link = driver.current_url
if "secure" in link:
    print("OK: Link 'secure' içeriyor.")
else:
    print("HATA: Link 'secure' içermiyor.")

sleep(2)

dogruMesaj = driver.find_element(By.CSS_SELECTOR, "h2").text
if "Secure Area" in dogruMesaj:
    print("OK: Sayfa başlığı doğru")
else:
    print("HATA: Sayfa başlığı yanlış")

sleep(2)

driver.find_element(By.XPATH, "//*[@id='content']/div/a").click()

sleep(2)

if "login" in driver.current_url:
    print("OK: Login sayfasına döndük.")
else:
    print("HATA: Login sayfasına dönmedi.")

sleep(2)

driver.quit()