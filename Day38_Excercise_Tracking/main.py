import requests
from datetime import datetime

APP_ID = "38a2a280"
APP_KEY = "3a39722bb7d231e2b8404a3864e8eb68"
FOOD_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

DETAIL = input("Tell me which exercise you did : ")

SHETTY_URL = "https://api.sheety.co/df978c2afaf427d0f42b5e952b70bd36/workoutTracking/workouts"


header1 = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
parameter = {
    "query": DETAIL,
    "gender": "male",
    "weight_kg": 68,
    "height_cm": 178,
    "age": 22
}
response = requests.post(FOOD_URL, json=parameter, headers=header1)
result = response.json()

today_date = datetime.now().strftime("%d%m%Y")
current_time = datetime.now().strftime("%X")
header = {
    "Authorization": "Basic eW9haG5lc2dldGluZXQ6MTIyMQ=="
}

for exercise in result["exercises"]:
    table_input = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHETTY_URL, json=table_input, auth=("yoahnes", "0000"))
    print(sheet_response.text)
