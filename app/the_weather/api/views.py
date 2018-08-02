from django.shortcuts import render
import requests
from django.views.generic.base import View

from the_weather.weather.forms import CityForm
from the_weather.weather.models import City


class CityWeatherView(View):
    def render(self, request):
        # city = 'New York'
        cities = City.objects.all()

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f6ef4a1203f873fc424005d4de801626'

        form = CityForm()

        weather_data = []

        for city in cities:
            # request the API data and convert the JSON to Python data types
            city_weather = requests.get(url.format(city)).json()

            weather = {
                'city': city,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon'],
            }
            # add the data for the current city into our list
            weather_data.append(weather)

        context = {'weather_data': weather_data, 'form': form}
        return render(request, 'weather.html', context)

    def get(self, request):
        return self.render(request)

    def post(self, request):
        form = CityForm(request.POST)  # add actual request data to form for processing
        if form.is_valid():  # only true if form is submitted
            form.save()  # will validate and save if validated
        return self.render(request)
