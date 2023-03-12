from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def about(request):
    return HttpResponse('Welcome to Lettle Lemon!') 

def menu(request):
    words = HttpResponse("Please look through Out Menu \n for a choice!") 
    return words 

