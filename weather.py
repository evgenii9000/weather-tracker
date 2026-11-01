import requests
from datetime import datetime, timezone

CITIES = ["Chisinau", "Bucharest", "London", "Stockholm"]

def main():
    with open("weather.log", "a", encoding="utf-8") as log_file:
        for city in CITIES:
            url = f"https://wttr.in/{city}?format=%t+%w+%h"
            ts = datetime.now(timezone.utc).isoformat()
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                weather = response.text.strip()

                if not weather or "Unknown location" in weather:
                    raise ValueError("bad weather response")

                log_file.write(f"{ts} | {city} | {weather}\n")
            except Exception as e:
                log_file.write(f"{ts} | {city} | ERROR: {e}\n")

if __name__ == "__main__":
    main()