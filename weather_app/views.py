from django.shortcuts import render
import requests
import json
import datetime
from weather_project.settings import API_KEY
from django.http import JsonResponse

def index(request):
    api_key = API_KEY
    current_weather_url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    if request.method == 'POST':
        body = json.loads(request.body)
        city = body.get('city')
        weather_data1= fetch_weather_and_forecast(city, api_key, current_weather_url)
        context = weather_data1
        return JsonResponse(context)
    else:
        return JsonResponse({'accessible':"yes"})


def fetch_weather_and_forecast(city, api_key, current_weather_url):
    url1 = current_weather_url.format(city, api_key)
    response = requests.get(url1).json()
    if response['cod'] == '404':
        return response
    weather_data = {
        'city': city,
        'temperature': round(response['main']['temp'] - 273.15),
        'description': response['weather'][0]['description'],
        'humidity':response['main']['humidity'],
        'wind':round(response['wind']['speed']),
        'main':response['weather'][0]['main'],
        'icon': response['weather'][0]['icon'],
    }
    return weather_data