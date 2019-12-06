from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def home(request):
    portfolio = Portfolio.objects
    return render(request, 'home.html',{'portfolios':portfolio})
