from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.innvictus.com/lanzamientos")

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ux-container"))
    )
    #nameSneaker1 = driver.find_element_by_xpath("/html/body/main/div[4]/div[4]/div/div[3]/a/div[3]/div/div[2]")
    #buttonBuy1 = driver.find_element_by_xpath("/html/body/main/div[4]/div[4]/div/div[3]/a/div[3]/button")
    #buttonState1 = buttonBuy1.text
    #nameSneaker2 = sneaker.find_element_by_xpath("/html/body/main/div[4]/div[4]/div/div[5]")
    nameSneaker2 = driver.find_element_by_xpath("/html/body/main/div[4]/div[4]/div/div[5]/a/div[3]/div/div[2]")
    buttonBuy2 = driver.find_element_by_xpath("/html/body/main/div[4]/div[4]/div/div[5]/a/div[3]/button")
    buttonState2 = buttonBuy2.text
    #print(nameSneaker1.text)
    #print(buttonBuy1.text, "\n")
    #print(nameSneaker2.text)
    #print(buttonBuy2.text)
    if(buttonState2 == "COMPRAR"):
        print(nameSneaker2.text, "\t", buttonBuy2.text, "\t", "Released")

            #Opening released tab. (Gives access denied)
            #driver.execute_script("window.open('');")
            #driver.switch_to.window(driver.window_handles[1])
            #driver.get('https://www.innvictus.com/p/000000000000213889')
            #time.sleep(1)
            #driver.switch_to.window(driver.window_handles[0])
    else:
        print(nameSneaker2.text, "\t", buttonBuy2.text, "\t", "Not released yet")
            
finally:
    driver.close()