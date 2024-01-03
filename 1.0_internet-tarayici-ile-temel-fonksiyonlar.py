# Selenium kütüphanesinden gerekli modülleri import ediyoruz
from selenium import webdriver
# Selenium'un Python'daki WebDriver'ını kullanabilmek için bu satırı ekleriz.
from selenium.webdriver.chrome.service import Service as ChromeService
# Chrome tarayıcısının servis yapılandırmasını özelleştirmek için bu satırı ekleriz.
from webdriver_manager.chrome import ChromeDriverManager
# webdriver_manager modülünden ChromeDriver'ı otomatik olarak yöneten sınıfı içe aktarır.
# Bu, tarayıcı sürücülerini otomatik olarak yönetmeyi sağlar.

# Chrome WebDriver'ı otomatik olarak yönetilir ve başlatılır
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://www.apple.com")  # Apple.com sayfasına gidilir
link = driver.current_url  # Geçerli URL alınır
baslik = driver.title  # Sayfa başlığı alınır
print("Sayfa başlığı: " + baslik)  # Sayfa başlığını ekrana yazdırır
if "apple.com" in link:  # Geçerli URL içinde "apple.com" kelimesi var mı diye kontrol eder
    print("Apple sayfasındayız: " + link)  # Eğer URL içinde "apple.com" kelimesi varsa, ekrana bir mesaj yazdırır

# Pencereyi maksimize etme
driver.maximize_window()

driver.get("http://www.etsy.com")  # Etsy.com sayfasına gidilir
link = driver.current_url  # Geçerli URL alınır
baslik = driver.title  # Sayfa başlığı alınır
print("Sayfa başlığı: " + baslik)  # Sayfa başlığını ekrana yazdırır
if "etsy.com" in link:  # Geçerli URL içinde "etsy.com" kelimesi var mı diye kontrol eder
    print("Etsy sayfasındayız: " + link)  # Eğer URL içinde "etsy.com" kelimesi varsa, ekrana bir mesaj yazdırır

driver.back()  # Geri gitme

baslik = driver.title  # Şu anki sayfanın başlığını alır
if "Apple" in baslik:  # Başlıkta "Apple" kelimesi var mı diye kontrol eder
    print("Apple sayfasına döndünüz")  # Eğer başlıkta "Apple" kelimesi varsa, ekrana bir mesaj yazdırır

# Şu anki pencereyi kapatma (tek sekmeli senaryo)
driver.close()

# Eğer birden fazla sekme varsa, bütün sekmeleri kapatır ve WebDriver'ı sonlandırır.
# driver.quit 
