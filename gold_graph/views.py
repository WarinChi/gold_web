from django.shortcuts import render, HttpResponse
from django.contrib.auth import login

def custom_login(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return HttpResponse('User not found')
