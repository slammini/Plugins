from flask import Flask, send_from_directory, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_home():
    return "Hello, World!"


@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get('input')
    if not location:
        return "Please provide a location parameter."
    # Replace 'your_api_key' with your actual OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=YOUR_OPENWEATHERMAP_API_KEY&units=metric"
    response = requests.get(url)
    data = response.json()
    if 'weather' in data and 'main' in data:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        humidity = data['main']['humidity']
        return f"The weather in {location} is {weather} with a temperature of {temperature}°C. The minimum temperature is {temp_min}°C, the maximum temperature is {temp_max}°C, and the humidity is {humidity}%."
    else:
        return f"Could not get weather data for {location}."



# Create a route named /.well-known/ai-plugin.json to access the ai-plugin.json file

@app.route('/.well-known/ai-plugin.json', methods=['GET'])
def serve_ai_plugin():
    return send_from_directory('.', 'ai-plugin.json', mimetype='application/json')


# Create a route named /.well-known/openapi.yaml to access the openapi.yaml file
@app.route('/.well-known/openapi.yaml', methods=['GET'])
def serve_openapi():
    return send_from_directory('.', 'openapi.yaml', mimetype='text/yaml')


# Create a route so that when i type "http://localhost:5000/logo.png" I can see my logo.png image
@app.route('/logo.png', methods=['GET'])
def serve_logo():
    return send_from_directory('.', 'logo.png', mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True, port=5000)




