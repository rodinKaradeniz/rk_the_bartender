import requests
import json

data = json.load(open("key_config.json"))
API_KEY = data["KEYS"]['api_key_openweather']

# get coordinates by location info - format: city, state code, country code, limit (optional), api key
API_URL_GEO = "http://api.openweathermap.org/geo/1.0/reverse?lat={}&lon={}&limit=1&appid={}"

# get weather by coordinates - format: latitude, longitude, api key
API_URL_WEATHER = "https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}&units=metric"


def api_get_weather(lat, lon):
    try:
        weather_data = requests.get(API_URL_WEATHER.format(lat, lon, API_KEY)).json()
        loc_data = requests.get(API_URL_GEO.format(lat, lon, API_KEY)).json()
        weather_info = {
            'city' : loc_data[0]['name'],
            'country': loc_data[0]['country'],
            'weather' : weather_data['weather'][0]['main'],
            'temperature' : str(round(weather_data['main']['temp'])) + '°C'
        }
        return weather_info

    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(api_get_weather(51.5098, -0.1180))