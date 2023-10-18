import requests

API_KEY = ""

# get weather by U.S. zip code
API_URL = ('http://api.openweathermap.org/data/2.5/weather?zip={},us&mode=json&units=imperial&appid={}')

def weather_query_api(zip):
    """submit the API query using variables for zip and API_KEY"""
    try:
        # print(API_URL.format(zip, API_KEY))
        data = requests.get(API_URL.format(zip, API_KEY)).json()

    except Exception as exc:
        print(exc)
        data = None

    return data