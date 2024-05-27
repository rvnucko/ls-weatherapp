from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.

def home(request):
    if 'city' in request.GET:
        city = request.GET['city']
        api_key = "b18920447a8d00cb0dacc317061f9975"
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"


        weather_response = requests.get(weather_url).json()
        forecast_response = requests.get(forecast_url).json()

        context = {
                'city': city,
                'temperature': weather_response['main']['temp'],
                'description': weather_response['weather'][0]['description'],
                'forecast': forecast_response['list'][0:5]
            }
    else:
        context = {}  
          
    return render(request, 'forecastweb/home.html', context)

def greet(request):
    return HttpResponse("Hello from LogiScool server!")

def hello(request, first_name):
    return render(request, 'forecastweb/hello.html', {'name': first_name})