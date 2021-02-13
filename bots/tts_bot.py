'''
AUTHOR: JakeSJK64
DATE: 2:25PM 13/02/2021
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

LANG = "ja"
TEXT_FILE = "text_speech.txt"
FILENAME = "voice.mp3"
URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "a538092306cf6de786078c0681f6855f"
CITY_NAME = "Kuala Lumpur"
complete_url = URL + "appid=" + API_KEY + "&q=" + CITY_NAME 
response = requests.get(complete_url)
response_json = response.json()


if response_json['cod'] != "404":
    y = response_json['main']
    current_temperature = int(y['temp'] - 273.15)
    current_pressure = int(y['pressure'] * 100)
    current_humidity = y['humidity']
    
    # store value of weather key in variable z
    z = response_json['weather']
    
    weather_description = z[0]['description']
    
    translator = Translator()
    
    message = ""
    
    if LANG == 'en':
        message = f"""
            Temperature: {current_temperature} degrees Celcius 
            Pressure: {current_pressure} Pascals
            Humidity: {current_humidity} %
            Description: {weather_description}         
        """
        write_to_file(TEXT_FILE, str(message))
        
    elif LANG == 'ja':        
        message = f"""
            温度: {current_temperature} 度、
            気圧: {current_pressure} パスカル、
            湿度: {current_humidity} %                   
        """     
    
    print(message)
    tts = gTTS(text=message,lang=LANG)
    tts.save(FILENAME)
    playsound.playsound(FILENAME)
    
else: 
    print("City Not Found!")




# def authenticate_google():
    # """Shows basic usage of the Google Calendar API.
    # Prints the start and name of the next 10 events on the user's calendar.
    # """
    # creds = None
    # # The file token.pickle stores the user's access and refresh tokens, and is
    # # created automatically when the authorization flow completes for the first
    # # time.
    # if os.path.exists('token.pickle'):
        # with open('token.pickle', 'rb') as token:
            # creds = pickle.load(token)
    # # If there are no (valid) credentials available, let the user log in.
    # if not creds or not creds.valid:
        # if creds and creds.expired and creds.refresh_token:
            # creds.refresh(Request())
        # else:
            # flow = InstalledAppFlow.from_client_secrets_file(
                # 'credentials.json', SCOPES)
            # creds = flow.run_local_server(port=0)
        # # Save the credentials for the next run
        # with open('token.pickle', 'wb') as token:
            # pickle.dump(creds, token)

    # return build('calendar', 'v3', credentials=creds)

    
# def get_events(n, service):
    # # Call the Calendar API
    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # print('Getting the upcoming {} events'.format(n))
    # events_result = service.events().list(calendarId='primary', timeMin=now,
                                        # maxResults=n, singleEvents=True,
                                        # orderBy='startTime').execute()
    # events = events_result.get('items', [])

    # if not events:
        # print('No upcoming events found.')
    # for event in events:
        # start = event['start'].get('dateTime', event['start'].get('date'))
        # print(start, event['summary'])


# service = authenticate_google()
# get_events(2, service)

# f = open('C:\\Users\\Shirley\\Desktop\\python\\bots\\speech_text.txt', "r", encoding='utf-8').read()
# tts = gTTS(text=str(f) ,lang="en")
# tts.tokenizer_func(str(f))
# filename = "voice.mp3"
# tts.save(filename)
# playsound.playsound(filename)