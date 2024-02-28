from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = '958d279306321786e0aa2e9718d73d27'
# OpenWeatherMap API endpoint
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city, units='metric'):
    params = {
        'q': city,
        'units': units,
        'appid': API_KEY,
    }
    response = requests.get(API_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return weather
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form.get('city')
        units = request.form.get('units')
        weather = get_weather(city, units)
        if weather:
            return render_template('index.html', weather=weather)
        else:
            return render_template('index.html', error='City not found!')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
