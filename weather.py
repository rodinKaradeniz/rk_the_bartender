import requests
import json

data = json.load(open("key_config.json"))
API_KEY = data["KEYS"]['api_key_openweather']

# get coordinates by location info - format: city, state code, country code, limit (optional), api key
API_URL_GEO = "http://api.openweathermap.org/geo/1.0/direct?q={},{},{}&limit={}&appid={}"

# get weather by coordinates - format: latitude, longitude, api key
API_URL_WEATHER = 'https://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'

def geocode_query_api(city='Toronto', state="ON", country="CA"):
    """submit the API query using variables for the location info and API_KEY"""
    try:
        # print(API_URL.format(zip, API_KEY))
        data = requests.get(API_URL_GEO.format(city, state, country, "", API_KEY)).json()[0]
        lat, lon = data['lat'], data['lon']
        return lat, lon

    except Exception as e:
        print(e)

def weather_query_api(city='Toronto', state="ON", country="CA"):
    """submit the API query using variables for zip and API_KEY"""
    try:
        # print(API_URL.format(zip, API_KEY))
        lat, lon = geocode_query_api(city, state, country)
        data = requests.get(API_URL_WEATHER.format(lat, lon, API_KEY)).json()
        location = data['name']
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f"Location: {location}, Weather: {weather}, Temperature: {temperature} degrees Fahrenheit"

    except Exception as e:
        print(e)

if __name__ == '__main__':
    print(geocode_query_api())
    print(weather_query_api())