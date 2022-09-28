from django.shortcuts import render, redirect
from . models import task
from django.contrib.auth import login as ulogin, authenticate, logout as ulogout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            ulogin(request, user)
            return redirect('/')
        else:
            print("invalid")

    return render(request, 'login.html')


def logout(request):
    ulogout(request)
    return redirect('/')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('psw1')
        password2 = request.POST.get('psw2')
        insert = User.objects.create_user(
            username=name, first_name=name, email=email, password=password1)
        insert.save()
    return render(request, 'signup.html')

# @login_required(login_url='login')


def addtask(request):
    if request.method == 'POST':
        tasktitle = request.POST.get('tasktitle')
        taskdesc = request.POST.get('taskDesc')
        insert = task(tasktitle=tasktitle, taskdesc=taskdesc)
        insert.unique_user = request.user
        insert.save()
    return render(request, 'todolist.html',)


def updatetask(request):
    return render(request, 'update todo.html')


def viewtask(request):
    if request.user.is_authenticated:
        user = request.user
        tasks = task.objects.filter(unique_user=user)
    else:
        return redirect('login')
    return render(request, 'viewtask.html', {'tasks': tasks})


def contact(request):
    return render(request, 'contact.html')
