'''
AUTHOR: JakeSiewJK64
DATE: 4:12PM 13/02/2021
'''
from __future__ import print_function
from gtts import gTTS
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googletrans import Translator

import os
import time
import playsound
import speech_recognition as sr
import requests
import datetime
import pickle
import os.path
import pyttsx3


def write_to_file(FILENAME, message):
    f = open(FILENAME, 'w', encoding='utf-8')
    f.write(message)
    f.close()

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

API_KEY = "YOUR_API_KEY_HERE"


TEXT_FILE = "text_speech.txt"
FILENAME = "voice.mp3"
URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY_NAME = "Sapporo"
complete_url = URL + "appid=" + API_KEY + "&q=" + CITY_NAME 
response = requests.get(complete_url)
response_json = response.json()
LANG = "ja" # <------ Change Language Here


if response_json['cod'] != "404":     
    
    # declaring Google Translate Object
    translator = Translator()
    
    y = response_json['main']    

    
    # calculate time
    time = time.localtime(time.time()).tm_hour + 1 
    
    current_location = response_json['sys']['country'] + ", " + response_json['name']     
    current_temperature = int(y['temp'] - 273.15) 
    current_pressure = int(y['pressure'] * 100)
    current_humidity = y['humidity']
    current_feels_like = int(y['feels_like'] - 273.15)
    current_wind_speed = int(response_json['wind']['speed'])
    
    current_visibility = response_json['visibility'] / 1000 
    
    # store value of weather key in variable z
    z = response_json['weather']
    
    weather_description = z[0]['description']   
    
    message = ""
    
    if LANG == 'en':
        postfix = "PM" if time > 12 else "AM"
        current_time = str(abs(12 - time)) + " " + postfix
        message = f"""
            Location: {current_location} 
            Time: {current_time}
            Temperature: {current_temperature} degrees Celcius 
            Feels like: {current_feels_like} degrees Celcius
            Pressure: {current_pressure} Pascals
            Humidity: {current_humidity} %
            Wind Speed: {current_wind_speed} km/s
            Visibility: {current_visibility} km
            Description: {weather_description}              
        """
        
    elif LANG == 'ja':  
        postfix = "午後" if time > 12 else "午前"
        current_time = postfix + " " + str(abs(12 - time)) + "時"
        message = f"""
            場所: {current_location}
            時間: {current_time}
            温度: {current_temperature} 度
            感じ: {current_feels_like} 度
            気圧: {current_pressure} パスカル
            湿度: {current_humidity} %
            視程: {current_visibility} km
            説明: {translator.translate(weather_description, src='en', dest=LANG).text} 
        """     
    
    print(message)
    tts = gTTS(text=message,lang=LANG)
    tts.save(FILENAME)
    playsound.playsound(FILENAME)
    
else: 
    print("City Not Found!")
