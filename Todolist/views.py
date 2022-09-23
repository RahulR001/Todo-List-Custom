from django.shortcuts import render
from . models import task, user
from django.contrib.auth import login,authenticate

def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('psw')
        user1 = user.objects.filter(username=username,password1=password)
        print('user valid')
        login(request,user1)
    
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('psw1')
        password2 = request.POST.get('psw2')
        insert = user(name=name, username=username, email=email,
                      password1=password1, password2=password2)
        insert.save()
    return render(request, 'signup.html')


def addtask(request):
     
    if request.method == 'POST':
        tasktitle = request.POST.get('tasktitle')
        taskdesc = request.POST.get('taskDesc')
        ls=task(tasktitle=tasktitle, taskdesc=taskdesc)
        ls.save()
    return render(request, 'todolist.html',  )


def updatetask(request):
    return render(request, 'update todo.html')


def viewtask(request):
    return render(request, 'viewtask')


def contact(request):
    return render(request, 'contact.html')
