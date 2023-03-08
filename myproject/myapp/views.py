from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse 

def drinks(request, drink_name):

    drink_items = {
        'Mocha':'A tpe of coffee',
        'Tea':'A type of beverage',
        'Lemonade': 'A type of refreshment'
    }
    choice_of_drinks = drink_items[drink_name]
    return HttpResponse(f"<h2> {drink_name}</h2>" + choice_of_drinks)
