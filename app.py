import requests
import configparser
from flask import Flask, render_template, request, json as flask_json
from dynaconf import FlaskDynaconf
from data import get_form_data, load_json

app = Flask(__name__)
FlaskDynaconf(app, settings_files=["settings.toml"])

@app.route('/')
def weather_dashboard():
    return render_template("home.html")

@app.route('/results', methods=['POST'])
def render_results():
    city, mock = get_form_data(request)
    if mock:
        data = load_json()
    else:
        data = get_weather_results(city, app.config.KEY)
    response = app.response_class(
        response=flask_json.dumps(data),
        mimetype='application/json'
    )
    return response


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']

def get_weather_results(city, key):
    api_url= f"{app.config.API_URL}weather?q={city}&units=metric&appid={key}"
    r= requests.get(api_url)
    return r.json()

if __name__ == '__main__':
    app.run()