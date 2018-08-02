from django.urls import path

from the_weather.api.views import index

app_name = 'api'

urlpatterns = [
    path('', index, name='index')
]
