from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
OPENWEATHERMAP_API_KEY = '958d279306321786e0aa2e9718d73d27'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        city_name = request.form['city']
        weather_data = get_weather_data(city_name)
        return render_template('weather.html', weather_data=weather_data)

    return render_template('index.html')

def get_weather_data(city_name):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHERMAP_API_KEY}'
    response = requests.get(api_url)
    weather_data = response.json()

    if response.status_code == 200:
        # Extract relevant information
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        return {'temperature': temperature, 'description': description}
    else:
        return None

if __name__ == '__main__':
    app.run(debug=True)
