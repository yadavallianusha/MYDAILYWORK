import requests   # Import requests library to make HTTP requests

API_KEY ="eb867404243498ab95344ec940642ba7"   # Your API key

city = "Bangalore"  # city name

# Create the API request URL with city, API key, and metric units
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Send GET request to the weather API
res = requests.get(url)

# Convert response data to JSON format
data = res.json()

# Check if the request was successful
if res.status_code == 200:
    print("City:", data["name"])  # Print city name
    print("Temp:", data["main"]["temp"], "°C")  # Print temperature in Celsius
else:
    print("City not found")  # Error message if city is not found
