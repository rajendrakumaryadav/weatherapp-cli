import requests
import yaml

report = None


def get_api_key() -> str | None:
    """
    This function reads the config.yaml file and returns the API key for OpenWeatherMap.
    :return: API key for OpenWeatherMap or None if not found.
    """
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
        if config:
            return config['weather']['openweather']['api_key']
    return None


def get_unit() -> str:
    """
    This function reads the config.yaml file and returns the unit for OpenWeatherMap.
    :return: unit for OpenWeatherMap or None if not found.
    """
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)
        if config:
            return config['weather']['openweather']['units']
    return 'metric'


def get_weather(city):
    if not get_api_key():
        return "Error: API key not found."
    base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={get_api_key()}&units={get_unit()}"

    response = requests.get(base_url)
    data = response.json()
    if response.status_code == 200:
        global report
        main = data['main']
        wind = data['wind']

        # gather data
        city_name = data['name']
        weather_desc = data['weather'][0]['description']
        humidity = main['humidity']
        pressure = main['pressure']
        wind_speed = wind['speed']

        # print data
        report = f"Weather report for {city_name}:\n" \
                 f"Description: {weather_desc}\n" \
                 f"Humidity: {humidity}\n" \
                 f"Pressure: {pressure}\n" \
                 f"Wind Speed: {wind_speed}\n"
    else:
        report = f"Error: {data['message']}"

    return report
