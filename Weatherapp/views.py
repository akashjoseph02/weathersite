from django.shortcuts import render

# Create your views here.

import requests

import urllib.request
import json

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city +'&units=metric&appid=c5ea1d8df3cea1e010d7e88d71ced552').read()
        list_data = json.loads(source)

        data = {
            "location" : city,
            # "country_code" : str(list_data['sys']['country']),
            "temp" : str(list_data['main']['temp']) + ' °C',
            "pressure" : str(list_data['main']['pressure']),
            "humidity" : str(list_data['main']['humidity']),
            "main" : str(list_data['weather'][0]['main']),
            "description" : str(list_data['weather'][0]['description']),
            "icon" : str(list_data['weather'][0]['icon']),
        }
        print(data)

    else:
        data = {}

    return render(request, "index.html", data)
        

