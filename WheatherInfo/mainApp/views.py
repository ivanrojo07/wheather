from django.shortcuts import render

from .models import City
from .forms import CityForm
import requests
import os


# Create your views here.

def index(request):
    cities = City.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api}'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    weather_data = []

    for city in cities:
        city_weather = requests.get(url.format(city=city,api=os.getenv("WHEATER_API_KEY",""))).json()

        weather = {
            'city' : city,
            'temperature' : city_weather['main']['temp'] if 'main' in city_weather else "",
            'description' : city_weather['weather'][0]['description'] if 'weather' in city_weather else '',
            'icon' : city_weather['weather'][0]['icon'] if 'weather' in city_weather else '',
            'humidity' : city_weather['main']['humidity'] if 'main' in city_weather else "",
            'pressure' : city_weather['main']['pressure'] if 'main' in city_weather else "",
            'country' : city_weather['sys']['country'] if 'sys' in city_weather else '',
            'sunrise' : city_weather['sys']['sunrise'] if 'sys' in city_weather else '',
            'sunset' : city_weather['sys']['sunset'] if 'sys' in city_weather else '',
            'windspeed': city_weather['wind']['speed'] if 'wind' in city_weather else ''
        }
        weather_data.append(weather)

    context = { 'weather_data' : weather_data, 'form': form }
    return render(request, 'index.html', context)