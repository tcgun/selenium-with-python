from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

def login(username, password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    mesaj = driver.find_element(By.ID, "flash").text
    return mesaj

mesaj = login("mauro", "SuperSecretPassword!")

if "Your username is invalid!" in mesaj:
    print("HATA: Yanlış kullanıcı adı doğru çalışıyor.")
else:
    print("OK: Yanlış kullanıcı adı çalışmıyor.")

mesaj = login("tomsmith", "icardi")

if "Your password is invalid!" in mesaj:
    print("HATA: Yanlış şifre doğru çalışıyor.")
else:
    print("OK: Yanlış şifre çalışmıyor.")

mesaj = login("tomsmith", "SuperSecretPassword!")

if "You logged into a secure area!" in mesaj:
    print("OK: Bilgiler doğru.")
else:
    print("HATA: Bilgiler yanlış.")

link = driver.current_url
if "secure" in link:
    print("OK: Link secure içeriyor.")
else:
    print("HATA: Link secure içermiyor.")

driver.quit()