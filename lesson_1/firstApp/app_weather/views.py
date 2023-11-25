from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def app_weather(request, *args, **kwargs):
     return HttpResponse(f'The weather is fine today!')
