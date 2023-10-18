from flask import Flask, render_template
from weather import weather_query_api

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template("index.html")
    link = '<p><a href="weather/<zip>">Click here to get weather information</a></p>'
    return 'Welcome!'


@app.route('/user/<name>')
def user(name):
    # the curly braces {} hold a variable; when below runs,
    # the value will replace the braces and the variable name
    personal = f'<h1>Hello, {name}!</h1>'

    instruc = '<p>Change the name in the <em>browser address bar</em> \
        and reload the page.</p>'

    return personal + instruc

@app.route('/weather/<zip>')
def get_weather(zip):
    # get the json file from the OpenWeather API
    resp = weather_query_api(zip)

    # construct a string using the json data items for temp and description
    try:
        text = resp["name"] + " temperature is " + str(resp["main"]["temp"]) + " degrees Fahrenheit with " + resp["weather"][0]["description"] + "."
    except:
        text = "There was an error.<br>Did you include a valid U.S. zip code in the URL?"
    return text

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=4999, debug=True)