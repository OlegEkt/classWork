from django.shortcuts import render
from .models import Meal, Ingredient

# Create your views here.

def menu(request, *args, **kwargs):
    if request.method == 'GET':
        # meals = Meal.objects.all()
        meals = Meal.objects.prefetch_related('ingredient').all()
        # ingredients = Ingredient.objects.all()
        # return render(request, 'app_meal/index.html',
        #               context={'meals': meals, 'ingredients': ingredients})
        return render(request, 'app_meal/index.html',
                      context={'meals': meals})
