import requests
import datetime as dt
import os

GENDER = "male"
WEIGHT_KG = "60"
HEIGHT_CM = "164"
AGE = "29"

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("SHEET_ENDPOINT")
exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)
today_date = dt.datetime.now().date().strftime('%d/%m/%Y')
today_time = dt.datetime.now().time().strftime('%X')
print(os.environ.get("TOKEN"))
bearer_headers = {
        "Authorization": f"Bearer {os.environ.get('TOKEN')}"
    }

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

    print(response.text)
