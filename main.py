from flask import Flask, request, render_template, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from weather import weather_query_api
from cocktails import *
from functools import wraps
import json
import jwt
import datetime

app = Flask(__name__)

data = json.load(open("key_config.json"))
JWT_KEY = data["KEYS"]['jwt_key']

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        print(token)
        if not token:
            return jsonify({'message' : 'Token is missing'}), 403

        try:
            data = jwt.decode(token, JWT_KEY, algorithms=['HS512', 'HS256'])
        except Exception as inst:
            print(inst)
            return jsonify({'message' : 'Token is invalid'}), 403

        return f(*args, **kwargs)
    
    return decorated


@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this'})


@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'Only for users with valid tokens'})


# Dummy user database for illustration purposes
users = {
    'john_doe': generate_password_hash('secure_password'),
    'rodin_k': generate_password_hash('password')
}

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    username = auth.username
    password = auth.password

    if username in users:
        if check_password_hash(users[username], password):
            # Logged in correctly, generate the token, active for 30 minutes
            token = jwt.encode({'user' : auth.username, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, JWT_KEY)
            return jsonify({'token' : token, 'message' : 'Login successful'})
        else:
            return jsonify({'message' : 'Password is invalid'}), 401
    else:
        # return make_response('Could not verify', 401, { 'WWW-Authenticate' : 'Basic Realm="Login Required"'})
        return jsonify({'message' : 'Username not found'}), 401

@app.route('/', methods=['GET'])
def home():
    # return render_template("index.html")
    link = '<p><a href="/weather">Click here to get weather information</a></p>'
    return 'Welcome!' + "\n" + link


@app.route('/test', methods=['GET'])
def text_flask():
    # response = {
    #     "id": 1,
    #     "name": "rodin",
    #     "age": 25
    # }
    return jsonify(api_get_cocktail(cocktail_name='espresso martini'))


@app.route('/weather', methods=['GET'])
def get_weather(city='Toronto', state="ON", country="CA"):
    """get the weather info from the OpenWeather API"""
    resp = weather_query_api(city, state, country)

    try:
        # get the weather info from the OpenWeather API
        resp = weather_query_api(city, state, country)

    except Exception as e:
        print(e)

    return resp


@app.route('/cocktail/<name>', methods=['GET'])
def get_cocktail(name):
    """get cocktail info from the cocktaildb API"""
    try:
        cocktail = api_get_cocktail(name)

    except Exception as e:
        print(e)
        return None

    return cocktail


@app.route('/randomCocktail', methods=['GET'])
def get_random_cocktail():
    """get a random cocktail info from the cocktaildb API"""
    try:
        cocktail = api_get_random_cocktail()

    except Exception as e:
        print(e)
        return None

    return cocktail


@app.route('/ingredient/<name>', methods=['GET'])
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
    # get_cocktail("margarita")
    # app.run(host='127.0.0.1', port=4999, debug=True)