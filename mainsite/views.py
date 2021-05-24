from django.shortcuts import render
# from .models import LocalDelivery,Store
# Create your views here.
def index(request):
    return render(request,'mainsite/index.html')


def calculator(request):
 return render(request,'mainsite/calculator.html')
