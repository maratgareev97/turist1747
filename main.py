from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D
from tensorflow.python.keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing import image
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import telebot
from os import listdir
import os
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
from multiprocessing import Process
import asyncio
import json
import requests
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
import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse
try:
    from main import distribution_dataset
    from main import *
except:
    print("")
def is_valid(url):
    """
    Checks whether `url` is a valid URL.
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

def get_all_images(url):
    """
    Returns all image URLs on a single `url`
    """
    soup = bs(requests.get(url).content, "html.parser")
    urls = []
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            # if img does not contain src attribute, just skip
            continue
        img_url = urljoin(url, img_url)
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        if is_valid(img_url):
            urls.append(img_url)
    return urls
def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024), f"Downloading {filename}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            # write data read to the file
            f.write(data)
            # update the progress bar manually
            progress.update(len(data))
def main(url, path):
    # get all images
    imgs = get_all_images(url)
    #print("imgs |",imgs)
    for img in imgs:
        # for each image, download it
        download(img, path)
def down2(list_img,number):
    d = 0
    for i in list_img:
        print("URL |",i)
        try:            
            f = str(d)
            driver.get(i)
            strr = "/home/keinn/Neron_net/download_foto"+number+"/"+f+".png"
            driver.save_screenshot(strr)
            d = d+1
            print(d)
        except: 
           print("ERROR")
def search(link):
    #filePath = "/home/keinn/Neron_net/download_foto2/0.png"
    filePath = link
    searchUrl = 'https://yandex.ru/images/search'
    files = {'upfile': ('blob', open(filePath, 'rb'), 'image/jpeg')}
    params = {'rpt': 'imageview', 'format': 'json', 'request': '{"blocks":[{"block":"b-page_type_search-by-image__link"}]}'}
    response = requests.post(searchUrl, params=params, files=files)
    query_string = json.loads(response.content)['blocks'][0]['params']['url']
    img_search_url= searchUrl + '?' + query_string
    #print(img_search_url)
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(executable_path=r'/home/keinn/Downloads/chromedriver_linux64/chromedriver',options=options)
    
    browser.get(url=img_search_url)
    try:
        name = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[1]').text
        last_name = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[3]').text
    except:
        name = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[1]').text
        last_name = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[2]').text
    if(last_name=='Википедия'):last_name = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[2]').text
    return name,last_name

def neural_network(input_shape):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(64))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(2))
    model.add(Activation('sigmoid'))

    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    return model
def train_():
    # Каталог с данными для обучения
    train_dir = 'train'
    # Каталог с данными для проверки
    val_dir = 'val'
    # Каталог с данными для тестирования
    test_dir = 'test'
    # Размеры изображения
    img_width, img_height = 150, 150
    image_size = (img_width, img_height)
    # Размерность тензора на основе изображения для входных данных в нейронную сеть
    # backend Tensorflow, channels_last
    input_shape = (img_width, img_height, 3)
    # Количество эпох
    epochs = 20
    # Размер мини-выборки
    batch_size = 16#16
    # Количество изображений для обучения
    nb_train_samples =16388 #17500
    # Количество изображений для проверки
    nb_validation_samples =3503 #3750
    # Количество изображений для тестирования
    nb_test_samples =3519#3750



    model = neural_network(input_shape)
                          
    datagen = ImageDataGenerator(rescale=1. / 255)

    train_generator = datagen.flow_from_directory(
        train_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='categorical')

    val_generator = datagen.flow_from_directory(
        val_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode='categorical')
        
    test_generator=datagen.flow_from_directory(
        test_dir,
        target_size=(img_width,img_height),
        batch_size=batch_size,
        class_mode='categorical')

    model.fit_generator(
        train_generator,
        steps_per_epoch=nb_train_samples // batch_size,
        epochs=epochs,
        validation_data=val_generator,
        validation_steps=nb_validation_samples // batch_size)

    scores = model.evaluate_generator(test_generator, nb_test_samples // batch_size)
    print("Аккуратность на тестовых данных: %.2f%%" % (scores[1]*100))

    try:model.save_weights("catvsdogs.h5")
    except:print("LOW")

def predict_():
    img_width, img_height = 150, 150
    input_shape = (img_width, img_height, 3)
    # Размер мини-выборки
    batch_size = 16#16

    model = neural_network(input_shape)                        
    datagen = ImageDataGenerator(rescale=1. / 255)

    test=datagen.flow_from_directory(
        'testone',
        target_size=(img_width,img_height),
        batch_size=batch_size,
        class_mode='categorical')


    model.load_weights("catvsdogs.h5")
    i = model.predict(test)
    print("ответ | ",np.argmax(i[0]))
    i = i[0]
    print(i)

flag = 0
bot = telebot.TeleBot('5244505272:AAHh_3Rv3DPdiA_zuQF-pr4-3BpLNUiDvHo')
@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    src = '/home/keinn/Neron_net/testone/' + file_info.file_path
    print(src)
    
    print("LLL")
    with open(src, 'wb') as new_file:
        new_file.write(downloaded_file)
    print("ура")
    #text = predict_()
    bot.reply_to(message,'Хотите узнать, что на картинке? Да')
    flag = 0
    try:
        @bot.message_handler(content_types=['text'])
        def after_text(message):
            if(message.text == 'Да'):
                try:
                    name = predict_()
                except:
                    print("hhhh")
                flag = 0
                link = listdir('/home/keinn/Neron_net/testone/photos/')
                link = link[-1]
                link = '/home/keinn/Neron_net/testone/photos/'+link

                #print("Link: ",link)
                try:
                    name,last_name = search(link)
                    bot.send_message(message.from_user.id,name)
                    bot.send_message(message.from_user.id,last_name)
                except:
                    bot.send_message(message.from_user.id,"не распознан объект")
                    msg = bot.send_message(message.from_user.id,"опишите объект")
                    #textt = msg.text
                    #print(textt)
                    main("https://yandex.com/images/","png")
                    flag = 1
                link_del = listdir('/home/keinn/Neron_net/testone/photos/')
                for i in link_del:
                    link = '/home/keinn/Neron_net/testone/photos/'+i
                    os.remove(link)
                print("DELETE_")
                print("end")
                link_del = listdir('/home/keinn/Neron_net/testone/photos/')
                for i in link_del:
                    link = '/home/keinn/Neron_net/testone/photos/'+i
                    os.remove(link)
                print("DELETE_")
                if(flag==0):bot.send_message(message.from_user.id,"Если объект неправильно распознан, напишите Нет?")
                flag = 0
            if message.text == 'Нет':
                print('my time')
                msg = bot.send_message(message.from_user.id, 'нейронная сеть добучается')
                main("https://yandex.com/images/","png")
                try:
                    download_foto2()
                    delete_sero_photo()
                    Rename()
                    sorted_osnov()
                    distribution_dataset.main()
                except:
                    print('hhh')

                train_()
            else:print("send")
    except:
        print("ERROR")    


                


bot.polling(none_stop=True)













