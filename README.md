# Weather App
This Python script fetches current weather information from the OpenWeatherMap API based on user input of a city name. It utilizes the requests library to send HTTP requests and retrieve JSON-formatted weather data. The user is prompted to enter the name of a city, and the script then makes a request to the OpenWeatherMap API to fetch the weather information for that city.

## Features:
Fetches weather information such as description and temperature for a specified city.
Converts temperature from Kelvin to Fahrenheit for better readability.
Handles errors gracefully in case the API request fails.
## How to Use:
- Clone the repository or download the weather_app.py file.
- Install the requests library if not already installed by running pip install requests.
- Run the script in your terminal or command prompt.
- Enter the name of the city for which you want to fetch the weather information.
- The script will display the current weather description and temperature for the specified city.
## Requirements:
- Python 3.x
- requests library
- OpenWeatherMap API:
To use this script, you'll need to sign up for an API key at OpenWeatherMap. Once you have your API key, replace the placeholder API_Key variable in the script with your actual API key.
