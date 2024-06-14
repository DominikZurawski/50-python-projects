""" Application save your sport activity in chosen Google Sheet Excel.
 You should type e.g.: Swam 3 hour
 Google Sheet should have defined headers like in sheety_config dictionary, e.g.: Date	Time	Exercise	Duration	Calories
"""
import requests
from datetime import datetime
import os

APP_ID = os.environ.get("APP_ID", "You should set APP ID. More on: https://developer.nutritionix.com/")
API_KEY = os.environ.get("API_KEY", "You should set API_KEY. More on: https://developer.nutritionix.com/")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "You should set API_KEY. More on: https://sheety.co/")

EXERCISES_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = 'https://api.sheety.co/b99932b2b78b1d2ffc748dad884d1bf8/myWorkouts/workouts'


sheety_headers= {
    "Content-Type": "application/json",
    "Authorization": SHEETY_TOKEN,
}


exercises_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

def add_activity():
    exercises_config = {
        "query": input("Tell me which exercise you did: ")
    }
    response = requests.post(url=EXERCISES_ENDPOINT, json=exercises_config, headers=exercises_headers)
    data = response.json()

    calories = data['exercises'][0]['nf_calories']
    exercise = data['exercises'][0]['name']
    duration = data['exercises'][0]['duration_min']

    add_excel_row(calories=calories ,exercise=exercise, duration=duration)


def add_excel_row(exercise, duration, calories):
    sheety_config = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise.title(),
            "duration": duration,
            "calories": calories,
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_config, headers=sheety_headers)
    data = response.json()


add_activity()


