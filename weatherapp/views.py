from django.shortcuts import render
import requests

def index(request):
    if 'city1' in request.POST:
        city=request.POST['city1']
    else:
        city='chennai'

    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=c362e110acb4ae5da508063256336576'
    PARAMS={'units':'metric'}
    data=requests.get(url,PARAMS).json()
    description=data['weather'][0]['description']
    icon=data['weather'][0]['icon']
    temp=data['main']['temp']

    return render(request,'index.html',{'description':description,'icon':icon,'temp':temp,'city':city})
