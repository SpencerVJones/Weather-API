# Weather API
This Python script fetches current weather information from the OpenWeatherMap API based on user input of a city name. It utilizes the requests library to send HTTP requests and retrieve JSON-formatted weather data. The user is prompted to enter the name of a city, and the script then makes a request to the OpenWeatherMap API to fetch the weather information for that city.


## Features:
- Fetches weather information such as description and temperature for a specified city.
- Converts temperature from Kelvin to Fahrenheit for better readability.
- Handles errors gracefully in case the API request fails.


## Usage:
- Obtain API Key: Sign up on OpenWeatherMap to get your API key.
- Clone the repository or download the `weather_app.py` file.
- Install the requests library if not already installed by running:
  ```
  pip3 install requests
  ```
- Run the Script: Execute the Python script in your terminal:
  ```
  weather_checker.py
  ```
- Enter City Name: When prompted, enter the name of the city for which you want to check the weather.
- View Weather Information: The script will display the current weather condition and temperature for the specified city.


## Limitations:
- This script provides weather information based on the data retrieved from the OpenWeatherMap API. Accuracy and availability of data may vary depending on the API service.
- The temperature is provided in Fahrenheit.


## Requirements:
- Python 3.x
- requests library
- OpenWeatherMap API:

## Technologies Used
- **Python**: The script is written in Python, a high-level programming language known for its simplicity and readability.
- **Requests Library**: The script utilizes the `requests` library, a popular HTTP library for Python, to interact with the OpenWeatherMap API. This library allows the script to make HTTP requests easily and handle responses effectively.
- **OpenWeatherMap API**: The script leverages the OpenWeatherMap API to retrieve current weather information for a specified city. This API provides various weather data, including temperature, humidity, wind speed, and weather conditions, based on geographical coordinates or city names.
- **IDE:** PyCharm

## Contributing
Contributions are welcome! 

### You can contribute by:
-  Reporting bugs
-  Suggesting new features
-  Submitting pull requests to improve the codebase
