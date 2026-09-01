import requests
from datetime import datetime

cities = ["Chisinau", "Bucharest", "London", "Stockholm"]

with open("weather.log", "a", encoding="utf-8") as log_file:
    for city in cities:
        url = f"https://wttr.in/{city}?format=%t+%w+%h"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                weather = response.text.strip()
                log_file.write(f"{datetime.now().isoformat()} | {city} | {weather}\n")
            else:
                log_file.write(f"{datetime.now().isoformat()} | {city} | ERROR\n")
        except Exception:
            log_file.write(f"{datetime.now().isoformat()} | {city} | FAIL\n")