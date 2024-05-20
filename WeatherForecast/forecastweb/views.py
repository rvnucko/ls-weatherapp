from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def home(request):

    city = "Martin"
    apiKey = "b18920447a8d00cb0dacc317061f9975"
    weatherURL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={apiKey}"
    forecastURL = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={apiKey}"

    weatherResponse = requests.get(weatherURL).json()
    forecastResponse = requests.get(forecastURL).json()

    context = {

        'city': city,
        'temperature': weatherResponse['main']['temp'],
        'description': weatherResponse['weather'][0]['description'],
        'forecast': forecastResponse['list'][0:5],

    }

    return render(request ,'forecastweb/home.html' ,context)

def greet(request):

    return HttpResponse("Hello from Logiscool Server!")

def hello(request ,firstName):

    return render(request ,'forecastweb/hello.html' ,{'name': firstName})