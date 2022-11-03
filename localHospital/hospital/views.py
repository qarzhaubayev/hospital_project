from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'accounts/homepage.html')

def administrator(request):
    return render(request, 'accounts/administrator.html')
def patient(request):
    return render(request, 'accounts/patient.html')