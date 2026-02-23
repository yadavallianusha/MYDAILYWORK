import requests

API_KEY = input("Enter YOUR_API_KEY: ")

city = input("Enter city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

res = requests.get(url)
data = res.json()

if res.status_code == 200:
    print("City:", data["name"])
    print("Temp:", data["main"]["temp"], "°C")
else:
    print("City not found")
