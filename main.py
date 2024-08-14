import selenium.webdriver as webdriver
#import self as self
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import js2py

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("https://www.instagram.com/accounts/login/")
wait = WebDriverWait(browser, 60)

sleep(8)
kul_ad=browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
kul_ad.send_keys('ruveydattr')#kullanıcı adı

sfr=browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
sfr.send_keys('snlun4513')#şifre

gırıs=browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]')
gırıs.click()

sleep(40)
browser.get("https://www.instagram.com/ruveydattr/")

sleep(3)
print("profile gidildi")

tkpci_sayisi = wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span")))
print(str([n.text for n in tkpci_sayisi]))

str_list = [n.text for n in tkpci_sayisi]
filtered_list = str_list[2:-2]
combined_str = ''.join(filtered_list)
result = int(combined_str)

takipci= wait.until(EC.element_to_be_clickable(
	(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a")))
takipci.click()
sleep(3)
print("takipçi listesine gidildi")

##### use set metod##############
pop_up_window = WebDriverWait(
        browser, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))

# Scroll till Followers list is there
"""
while True:
    browser.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
        pop_up_window)
    
    sleep(1)
"""

tkpci_sayisi = wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span")))
str([n.text for n in tkpci_sayisi])

str_list = [n.text for n in tkpci_sayisi]
filtered_list = str_list[2:-2]
result = int(filtered_list)

print(result)
takipciler=[]
for p in range(1,result+1):
    tkpcı_isim = wait.until(EC.presence_of_all_elements_located((By.XPATH,
         "/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[" + str(p) + "]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")))
    print(str(p) + "---" + str([i.text for i in tkpcı_isim]))
    takipciler.append(str([i.text for i in tkpcı_isim]))
    browser.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
        pop_up_window)



takipci_listesini_kapat= wait.until(EC.element_to_be_clickable(
	(By.XPATH,"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button/div/svg/line")))
takipci_listesini_kapat.click()
sleep(3)
print("takipçi listesi kapatıldı")

tkp_edilen_sayisi = wait.until(EC.presence_of_all_elements_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span")))
str([n.text for n in tkp_edilen_sayisi])
str_list2 = [n.text for n in tkp_edilen_sayisi]
filtered_list2 = str_list2[2:-2]
result2 = int(filtered_list2)
print(result2)

takip_edilen_listesi= wait.until(EC.element_to_be_clickable(
	(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[3]/div/a/span/span")))
takip_edilen_listesi.click()
sleep(3)
print("takip edilenler listesine gidildi")

pop_up_window2 = WebDriverWait(
        browser, 2).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]")))



takip_edilenler=[]
for t in range(1,result2+1):
    tkp_edilen_isim = wait.until(EC.presence_of_all_elements_located((By.XPATH,
         "/html/body/div[7]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[4]/div[1]/div/div[" + str(t) + "]/div/div/div/div[2]/div/div/div/div/div/a/div/div/span")))
    print(str(t) + "---" + str([n.text for n in tkp_edilen_isim]))
    takip_edilenler.append(str([n.text for n in tkp_edilen_isim]))
    browser.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
        pop_up_window2)
browser.quit()


set1 = set(takipciler)
set2 = set(takip_edilenler)

unfollowers=set1.difference(set2)#benim takip edip beni takip etmeyenler
not_followed_by_me=set2.difference(set1)#ben takip edmeyip beni takip edenler
mutual=set1.intersection(set2)#karşılıklı takipleşilenler
print(unfollowers)
print(mutual)
print(not_followed_by_me)