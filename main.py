from flask import Flask, render_template
from weather import weather_query_api
from cocktails import *

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template("index.html")
    link = '<p><a href="/weather">Click here to get weather information</a></p>'
    return 'Welcome!' + "\n" + link


@app.route('/user/<name>')
def user(name):
    # the curly braces {} hold a variable; when below runs,
    # the value will replace the braces and the variable name
    personal = f'<h1>Hello, {name}!</h1>'

    instruc = '<p>Change the name in the <em>browser address bar</em> \
        and reload the page.</p>'

    return personal + instruc


@app.route('/weather')
def get_weather(city='Toronto', state="ON", country="CA"):
    """get the weather info from the OpenWeather API"""
    resp = weather_query_api(city, state, country)

    try:
        # get the weather info from the OpenWeather API
        resp = weather_query_api(city, state, country)

    except Exception as e:
        print(e)

    return resp


@app.route('/cocktail/<name>', method=['GET'])
def get_cocktail(name):
    """get cocktail info from the cocktaildb API"""
    try:
        cocktail = api_get_cocktail(name)

    except Exception as e:
        print(e)
        return None

    return cocktail


@app.route('/randomCocktail', method=['GET'])
def get_random_cocktail():
    """get a random cocktail info from the cocktaildb API"""
    try:
        cocktail = api_get_random_cocktail()

    except Exception as e:
        print(e)
        return None

    return cocktail


@app.route('/ingredient/<name>', method=['GET'])
def get_ingredient(name):
    """get ingredient info from the cocktaildb API"""
    try:
        ingredient = api_get_ingredient(name)

    except Exception as e:
        print(e)
        return None

    return ingredient


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=4999, debug=True)