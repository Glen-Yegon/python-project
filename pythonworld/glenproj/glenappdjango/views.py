import json  
from django.shortcuts import render
import urllib.request

def index(request):
  if request.method == 'POST':
      city = request.POST['city']
      source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='
                                      + city + 
                                    '&units=metric&appid=b1b15e88fa797225412429c1c50c122a').read()
      list_of_data = json.loads(source)
    
      data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinates": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']),
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        "main": str(list_of_data['weather'][0]['main']),
        "description": str(list_of_data['weather'][0]['description']),
        "icon": list_of_data['weather'][0]['icon'],
      }
      print(data)
  else:
     data = {} 

  return render(request, 'index.html', data)

def new_func():
    return "coordinates"