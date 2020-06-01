from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values' : ['наш телефон:', '8-800-2000-500']})
    

# Create your views here.
