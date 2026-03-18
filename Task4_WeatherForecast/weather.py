import requests  # For API request

# Replace this with your real OpenWeather API key
API_KEY = input("YOUR_API_KEY: ")

# Take city input from user
city = input("Enter city name: ").strip()

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

try:
    # Send request
    res = requests.get(url)
    data = res.json()

    # Success condition
    if res.status_code == 200:
        print("\n----- Weather Details -----")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Feels Like:", data["main"]["feels_like"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])

    else:
        # Error from API
        if data.get("cod") == 401:
            print("Error: Invalid API key. Please check your API key.")
        elif data.get("cod") == "404":
            print("Error: City not found. Please check spelling.")
        else:
            print("Error:", data.get("message", "Something went wrong"))

# Network / connection error
except requests.exceptions.RequestException:
    print("Error: Unable to connect. Check your internet connection.")
