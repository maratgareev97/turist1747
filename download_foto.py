from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import os.path
import random
import wget 
import time
import sys
import urllib
from selenium.webdriver.chrome.options import Options
#
from multiprocessing import Process
import asyncio
print ('Headless')
_start = time.time()
options = Options()
options.add_argument("--headless") # Runs Chrome in headless mode.
options.add_argument('--no-sandbox') # # Bypass OS security model
options.add_argument('start-maximized')
options.add_argument('disable-infobars')
options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=options,executable_path=r'/home/keinn/Downloads/chromedriver_linux64/chromedriver')

#
url = "https://yandex.ru/images/search?from=tabbar&text="
search = input("Enter: ")
browser = webdriver.Chrome(executable_path=r'/home/keinn/Downloads/chromedriver_linux64/chromedriver')
browser.get(url=url + search + " картинки")
elm = browser.find_element_by_tag_name("html")
elm.send_keys(Keys.END)
time.sleep(60)
print("Нашел")

images = browser.find_elements_by_class_name('serp-item__link')
print(len(images))
list_img = ["null"]
for i in range(len(images)):
    src = images[i].get_attribute('href')
    src = src[src.find("https%")::]
    src = src[:src.find("&text"):]
    src = src.replace("%2F", "/")
    src = src.replace("%3A", ":")
    if src.find("&from=") != -1:
        src = src[:src.find("&from=") + 1:]
        list_img.append(src)
    if src.find("%3F") == -1:
        list_img.append(src)
        if list_img[-1]==list_img[-2]:
            list_img.pop(-1)
list_img.pop(0)

print(len(list_img))
for i in range(len(list_img)):
    list_img[i] = list_img[i].replace("&", "")
    proctriF = list_img[i].find("%3F")
    if proctriF != -1:
        list_img[i] = list_img[i][:proctriF + 1:]
    list_img[i] = list_img[i].replace("%", "")
    #print(list_img[i])


#print(list_img)

def down2(list_img):
    d = 0
    for i in list_img:
        print("URL |",i)
        try:            
            f = str(d)
            driver.get(i)
            strr = "/home/keinn/Neron_net/download_foto2/"+f+".png"
            driver.save_screenshot(strr)
            d = d+1
            print(d)
        except: 
           print("ERROR")

down2(list_img)




























def down(list_img,):
    i = index
    for url in list_img:
        try:   
            print(url)
            d = str(i)
            strr = "/home/keinn/Neron_net/download_foto3/"+d+".jpg"
            
            site = urllib.request.urlopen(url)
            print ((round((site.length / 1024),2) / 1024),"Mb")
            i = i+1
            wget.download(url, strr)
        except:
            print("ERROR")