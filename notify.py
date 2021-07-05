import requests
from datetime import datetime, timedelta
import json
import beepy
today = datetime.today()
import time
import pywhatkit as kit

num_days = 7
all_dates = []
for i in range(num_days):
    all_dates.append(today + timedelta(i))

# print(all_dates)

final_dates = []
for i in all_dates:
    final_dates.append(i.strftime("%d%m%y"))

while True:

    for d in final_dates[1:]:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}".format(
            560, d)

        result = requests.get(URL)
        # print(result.text)

        json_result = result.json()
        for session in json_result["sessions"]:
            if session["address"] == "Apollo Speciality Hospitals Chennai Bye - Pass Road  Ariyamangalam Old Palpannai Trichy" and session["min_age_limit"] == 45 and session["vaccine"] == "COVAXIN" and session["available_capacity_dose1"] > 0:
                beepy.beep(sound=1)
                kit.sendwhatmsg("+919003864281", "COVAXIN AVAILABLE AT APOLLO ")

    time.sleep(300)
