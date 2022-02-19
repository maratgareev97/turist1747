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
    print(img_search_url)
    browser = webdriver.Chrome(executable_path=r'/home/keinn/Downloads/chromedriver_linux64/chromedriver')
    browser.get(url=img_search_url)
    name = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[1]').text
    last_name = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/div[1]/div/section/div/div/div/div[3]').text
    return name,last_name,img_search_url

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
    if(i[0]>i[1]):
        print("cat")
        return 'cat'
    else:
        print('dog')
        return "dog"
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
    text = predict_()
    bot.reply_to(message,text+'  да/нет')
    @bot.message_handler(content_types=['text'])
    def after_text(message):
        if message.text == 'Нет':
            msg = bot.send_message(message.from_user.id, 'нейронная сеть добучается')
            #link = '/home/keinn/Neron_net/testone/' + file_info.file_path
            link = listdir('/home/keinn/Neron_net/testone/photos/')
            link = link[-1]
            link = '/home/keinn/Neron_net/testone/photos/'+link

            print("Link: ",link)
            try:
                name,last_name,url = search(link)
                
                bot.send_message(message.from_user.id,name)
                bot.send_message(message.from_user.id,last_name)
            except:
                bot.send_message(message.from_user.id,"не распознан объект")
            link_del = listdir('/home/keinn/Neron_net/testone/photos/')
            for i in link_del:
                link = '/home/keinn/Neron_net/testone/photos/'+i
                os.remove(link)
            print("DELETE_")
            print("end")

            #########################################################################



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
            search = name
            browser = webdriver.Chrome(executable_path=r'/home/keinn/Downloads/chromedriver_linux64/chromedriver')
            browser.get(url=url + search + " картинки")
            elm = browser.find_element_by_tag_name("html")
            elm.send_keys(Keys.END)
            time.sleep(1)
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
            


            number = 1
            print("number |",number)
            down2(list_img,number)











        if(message.text == 'Да'):
            link_del = listdir('/home/keinn/Neron_net/testone/photos/')
            for i in link_del:
                link = '/home/keinn/Neron_net/testone/photos/'+i
                os.remove(link)
            print("DELETE_")
bot.polling(none_stop=True)













