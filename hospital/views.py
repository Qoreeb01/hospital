#  
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')


def contact(request):
    return render(request, 'contact.html')

def appointment(request):
    return render(request, 'appointment.html')