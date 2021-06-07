from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from .models import Message
from django.http import HttpResponse


def login_page(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            return HttpResponse("Wrong Credentials!")

def logout_view(request):
    logout(request)
    return redirect(reverse('login_page'))


def index(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login_page'))
    if request.method=="POST":
        message = request.POST['message']
        new_message_object = Message(text=message)
        new_message_object.origin = request.user
        new_message_object.save()
    all_messages = Message.objects.all()
    return render(request, "index.html", {'messages': all_messages})