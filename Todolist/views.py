from django.shortcuts import render,redirect
from . models import task
from django.contrib.auth import login as ulogin,authenticate,logout
from django.contrib.auth.models import User 


def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('psw')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            ulogin(request, user)
            return redirect('/')
        else:
            print("invalid")
    
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('psw1')
        password2 = request.POST.get('psw2')
        insert = User.objects.create_user(username=name,first_name=name,email=email,password=password1)
        insert.save()
    return render(request, 'signup.html')


def addtask(request):
     
    if request.method == 'POST':
        tasktitle = request.POST.get('tasktitle')
        taskdesc = request.POST.get('taskDesc')
        insert=task(tasktitle=tasktitle, taskdesc=taskdesc)
        ls=insert.save(commit=False)
        ls.unique_user = request.user
        ls.save()
    return render(request, 'todolist.html',  )


def updatetask(request):
    return render(request, 'update todo.html')


def viewtask(request):
    return render(request, 'viewtask')


def contact(request):
    return render(request, 'contact.html')
