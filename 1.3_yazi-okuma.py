# Selenium kütüphanesinden gerekli modülleri içe aktar
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# WebDriver'ı başlatma ve pencereyi maksimize etme
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Wikipedia'nın Türkçe anasayfasına gitme
driver.get("https://tr.wikipedia.org/wiki/Anasayfa")

# Seçkin madde alanını bulma ve yazısını alma
seckinMaddeAlani = driver.find_element(By.ID, "mp-tfa")
seckinMaddeYazisi = seckinMaddeAlani.text

# Yazıdan gereksiz kısmı ayırma ve ekrana yazdırma
seckinMaddeYazisi = seckinMaddeYazisi.split(",")[0]
print("Seçkin Madde: " + seckinMaddeYazisi)

# Kaliteli maddeyi bulma ve yazısını alma
kaliteliMadde = driver.find_element(By.ID, "mf-tfp").text

# Yazıdan gereksiz kısmı ayırma ve ekrana yazdırma
kaliteliMadde = kaliteliMadde.split(",")[0]
print("Kaliteli Madde: " + kaliteliMadde)

# WebDriver'ı kapatma
driver.quit()