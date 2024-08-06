import selenium.webdriver as webdriver
import self as self
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import js2py

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36'
driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("https://www.instagram.com/accounts/login/")
wait = WebDriverWait(browser, 60)

sleep(20)
kul_ad=browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
kul_ad.send_keys('')#kullanıcı adı

sfr=browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
sfr.send_keys('')#şifre

gırıs=browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
gırıs.click()

sleep(40)
browser.get("https://www.instagram.com/ruveydattr/")

sleep(3)
print("profile gidildi")

takipci= wait.until(EC.element_to_be_clickable(
	(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")))
takipci.click()
takipci.getAttribute()
sleep(3)
print("takipçi listesine gidildi")

sayac=0
##### use set metod##############

pop_up_window = WebDriverWait(
    browser, 2).until(EC.presence_of_all_elements_located(
        (By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]")))
scroll_script = "arguments[0].scrollTop = arguments[0].scrollHeight;"

for p in range(1,150):
    tkpcı_isim = wait.until(EC.presence_of_all_elements_located((By.XPATH,
         "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[" + str(p) + "]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")))
    sayac += 1
    print(str(sayac) + "---" + str(i.text for i in tkpcı_isim))
    browser.execute_script(scroll_script, pop_up_window)
