from django.shortcuts import render


# Create your views here.
def index(request):
    response = render(request, 'wegame/home.html')
    return response

def about(request):
    response = render(request, 'wegame/about.html')
    return response

def login(request):
    response = render(request, 'wegame/login.html')
    return response

def logout(request):
    response = render(request, 'wegame/logout.html')
    return response

def register(request):
    response = render(request, 'registration/registration.html')
    return response

