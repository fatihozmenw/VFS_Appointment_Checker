from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import winsound
import datetime

driver = webdriver.Chrome()
driver.maximize_window()


#Login ekranı giriş bilgileri
USERNAME = "test@gmail.com"
PASSWORD = "şifre"

# Kaç saniyede 1 arama yapılacak - Sistem tek bir seçenek için en az 15 sn ihtiyaç duyuyor neredeyse. Bu yüzden 0.5 dk yaparsanız en fazla 2 alan için aratmalısınız 1 dakika için en fazla 4
REPEAT_TIME_IN_MINUTES = 1
#VFS Login Sayfası URL
VFS_GLOBAL_URL = "https://visa.vfsglobal.com/tur/en/pol/login"

#Bu alan VFS randevu ekranında belirlenen üç kısımı gösteriyor. Buradaki herbir liste elemanı websitesindeki menülerden belirtilen yazılarla eşlenendiğinde çalışıyor. 
#Kategorideki yazıların tamamının yazılmasına gerek yoktur fakat ayrım yapılabilecek kısımlar seçilmelidir. Seçilen kısım tamamiyle aynı yazılmalıdır eşleme için.
VFS_GLOBAL_CENTERS = ["Gaziantep", "Beyoglu", "Trabzon", "Izmir"]
VFS_GLOBAL_CATEGORY = ["(Type D)","(Type D)", "(Type C)","(Type D)"]
VFS_GLOBAL_SUB_CATEGORY= ["Work permit", "Work permit", "Business", "Work permit"]



#Her alan seçildiğinde ekrandaki yüklenme arasında geçen zaman eğer sistem yavaşsa artırılabilir yoksa bazı alanları belirtilen sürede bulamaz ise arama aksayabilir 
RESPOND_TIME_IN_SECONDS = 2 
#Sistem ilk açıldığında geçen süre eğer 6 belirlenmisse login ekranından giriş yapıldığında XX:XX:01 olacak şekilde ayarlandı
DELAY = 6

#Alarm süresi
ALARM_DURATION_IN_SECONDS = 60

#####################################################################################################################

REPEAT_TIME_IN_SCONDS = REPEAT_TIME_IN_MINUTES*60
minTen = (datetime.datetime.now().minute) % REPEAT_TIME_IN_MINUTES
totalSec = minTen*60 + datetime.datetime.now().second
waitTime = 0
waitTime = totalSec % REPEAT_TIME_IN_SCONDS
waitTime = totalSec % (REPEAT_TIME_IN_SCONDS-DELAY)
sleepTime = (REPEAT_TIME_IN_SCONDS-DELAY) - waitTime
time.sleep(sleepTime)


driver.get(VFS_GLOBAL_URL)

try:
    coockieAccept = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))).click()
except Exception as e:
    print(e)

while 1 > 0:

    oldTime = datetime.datetime.now()
    isFound = 0 > 1

    driver.get(VFS_GLOBAL_URL)
    
    while 1 > 0:
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-input-0"]')))
            break
        except Exception as e:
            driver.get(VFS_GLOBAL_URL)


    username = USERNAME
    password = PASSWORD
    

    try:
        time.sleep(1)
        username_Xpath = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
        username_Xpath.send_keys(username)
        time.sleep(1)
        password_Xpath = driver.find_element(By.XPATH, '//*[@id="mat-input-1"]')
        password_Xpath.send_keys(password)
        password_Xpath.send_keys(Keys.RETURN)
        time.sleep(2)
    except Exception as e:
        print(e)


    try:
        time.sleep(2)
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-dashboard/section/div/div[2]/button'))).click()
    except Exception as e:
        print(e)


    for x in range(len(VFS_GLOBAL_CENTERS)):        
        try:
            time.sleep(RESPOND_TIME_IN_SECONDS)
            centerXpath = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-0"]'))).click()
            cXpath = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(.,'"+ VFS_GLOBAL_CENTERS[x] +"')]"))).click()
            time.sleep(RESPOND_TIME_IN_SECONDS)
            typeXpath = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-2"]'))).click()
            tXpath = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(.,'" + VFS_GLOBAL_CATEGORY[x] +"')]"))).click()
            time.sleep(RESPOND_TIME_IN_SECONDS)
            altXpath = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mat-select-4"]'))).click()
            aXpath = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//mat-option/span[contains(.,'" + VFS_GLOBAL_SUB_CATEGORY[x] + "')]"))).click()
            
            try:
                WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-eligibility-criteria/section/form/mat-card[2]/button')))
                print("Appointment Found - "+ VFS_GLOBAL_CENTERS[x])
                print(datetime.datetime.now())
                isFound = 1>0
                break
            except Exception as e:
                print("Not Found - "+ VFS_GLOBAL_CENTERS[x])
        except Exception as e:
            print(e)

    if(isFound):
        break

    print("--------------------------")
    
    driver.get("https://google.com")

    newTime = datetime.datetime.now()
    
    sleepTime = round((newTime - oldTime).total_seconds())
    sTime = REPEAT_TIME_IN_SCONDS - (sleepTime % REPEAT_TIME_IN_SCONDS)
    time.sleep(sTime)

for x in range(ALARM_DURATION_IN_SECONDS):
    winsound.Beep(750, 1000)

time.sleep(3600)    
