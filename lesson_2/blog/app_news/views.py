import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def news_list(request, *args, **kwargs):
    data = {
        'date_now': datetime.datetime.now(),
        'news_categories' : ('Criminal', 'Politics', 'Sport')
    }
    return render(request, 'app_news/index.html', context=data)


