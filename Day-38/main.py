import requests
from datetime import datetime

APP_ID = "your app_id"
API_KEY = "your api_key"
MY_TOKEN = "your token"
GENDER = "Male"
WEIGHT_KG = 63
HEIGHT_CM = 156
AGE = 29

exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercie you did? ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(exercise_endpoints, json=parameters, headers=headers)
result = response.json()
# print(result)

sheet_endpoints = "your sheets_endspoints"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Basic authentication
    # sheet_response = requests.post(sheet_endpoints, json=sheet_inputs, auth=(my_user_name, my_password))

    # with Bearer Token authentication
    bearer_headers = {
        "Authorization": f"Bearer {MY_TOKEN}"
    }
    sheet_response = requests.post(sheet_endpoints, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)
