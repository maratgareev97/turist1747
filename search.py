import json

import requests

filePath = "/home/keinn/Neron_net/download_foto2/0.png"
searchUrl = 'https://yandex.ru/images/search'
files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
response = requests.post(searchUrl, params=params, files=files)
query_string = json.loads(response.content)['blocks'][0]['params']['url']
img_search_url= searchUrl + '?' + query_string
print(img_search_url)





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




browser = webdriver.Chrome(executable_path=r'/home/keinn/Downloads/chromedriver_linux64/chromedriver')
browser.get(url=img_search_url)
print(browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[1]').text)
print(browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[3]').text)


