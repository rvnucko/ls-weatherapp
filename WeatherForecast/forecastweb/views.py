from django.shortcuts import render, redirect
import requests
from datetime import datetime
import pytz

# Create your views here.

def redirect_home_page(request):
    return redirect('home_page')

def home_page(request):
    return render(request, 'forecastweb/home.html')

def forecast(request):
    if request.method == 'POST':
        city = request.POST.get('city')

        now = datetime.now(pytz.timezone('Europe/Bratislava'))
        dt_string = now.strftime("%d/%m/%Y %H:%M")

        api_key = "b18920447a8d00cb0dacc317061f9975"
    
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},SK&units=metric&appid={api_key}"
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city},SK&units=metric&appid={api_key}"

        resp_weather = requests.get(weather_url).json()
        resp_forecast = requests.get(forecast_url).json()

        temperature_now = round(resp_weather['main']['temp'])
        temperature_min = round(resp_weather['main']['temp_min'])
        temperature_max = round(resp_weather['main']['temp_max'])

        return render(request, 'forecastweb/forecast.html', {
            'city': city,
            'time': dt_string,
            'temp': temperature_now,
            'temp_min': temperature_min,
            'temp_max': temperature_max,
            })
    




# if 'city' in request.GET:
#         city = request.GET['city']
#         api_key = "b18920447a8d00cb0dacc317061f9975"
#         weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
#         forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={api_key}"


#         weather_response = requests.get(weather_url).json()
#         forecast_response = requests.get(forecast_url).json()

#         context = {
#                 'city': city,
#                 'temperature': weather_response['main']['temp'],
#                 'description': weather_response['weather'][0]['description'],
#                 'forecast': forecast_response['list'][0:5]
#             }
#     else:
#         context = {}  
          
#     return render(request, 'forecastweb/home.html', context)

# https://api.openweathermap.org/data/2.5/weather?q=Bratislava&units=metric&appid=b18920447a8d00cb0dacc317061f9975

# http://api.openweathermap.org/geo/1.0/direct?q=Martin,SK&appid=b18920447a8d00cb0dacc317061f9975