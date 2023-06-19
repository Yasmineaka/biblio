from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def books(request):
    return render(request, 'books.html')


def profile(request):
    return render(request, 'profile.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')
