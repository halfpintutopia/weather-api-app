from django.urls import path

# from the_weather.api.views import index
from the_weather.api.views import CityWeatherView

app_name = 'api'

urlpatterns = [
    path('', CityWeatherView.as_view(), name='index')
]
