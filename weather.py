import requests
from datetime import datetime

city = "Moscow"  # можешь заменить на свой город на латинице, например "London"

url = f"https://wttr.in/{city}?format=%t+%w+%h"

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        weather = response.text.strip()
        with open("weather.log", "a", encoding="utf-8") as f:
            f.write(f"{datetime.now().isoformat()} | {weather}\n")
        print("OK")
    else:
        print("Error")
except Exception as e:
    print("Fail")