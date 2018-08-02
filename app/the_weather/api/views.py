from django.shortcuts import render
import requests
from django.views.generic import TemplateView
from rest_framework.views import APIView


def index(request):
    template_name = 'weather.html'
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f6ef4a1203f873fc424005d4de801626'
    city = 'Los Angeles'
    city_weather = requests.get(url.format(city)).json()

    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon'],
    }

    context = {'weather': weather}
    return render(request, template_name, context)

# class CityWeatherView(TemplateView):
#     template_name = 'weather.html'
#     url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f6ef4a1203f873fc424005d4de801626'
#     city = 'Los Angeles'
#     city_weather = requests.get(url.format(city)).json()
#
#     weather = {
#         'city': city,
#         'temperature': city_weather['main']['temp'],
#         'description': city_weather['weather'][0]['description'],
#         'icon': city_weather['weather'][0]['icon'],
#     }
#     context = {'weather': weather}
#
#     def index(self, request):
#
#         return render(request, self.template_name, self.context)
