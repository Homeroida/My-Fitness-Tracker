import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = "115"
HEIGHT_CM = "191"
AGE = "34"

APP_ID = "f32daea5"
API_KEY = "be2b77e4d2dea317105920b5cda551ca"
SHEETY_TOKEN = "Bearer sd8f76sdf786sd5f8s5d4f68s5d4f4sd4fs658df8sd5f"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/5da7b4752f760b51c97ddcf581754376/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "Authorization": SHEETY_TOKEN
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)
