# In terminal > pip install request
import requests

API_Key = "2b51fbdbc86edd54e785e6b5be28b998"  # https://openweathermap.org/
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"  # Where we are sending the request to

# Query Parameters
city = input("Enter Your City: ")
requests_url = f"{BASE_URL}?appid={API_Key}&q={city}"
response = requests.get(requests_url)

if response.status_code == 200:
    data = response.json()
    # print(data)
    weather = data["weather"][0]["description"]
    print("Weather:", weather)
    temperature = data["main"]["temp"]
    formatted_temperature = round((temperature - 273.15) * 1.8 + 32)
    print("Temperature:", formatted_temperature)

else:
    print("An error has occurred")

