from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from writings.views import show
# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == "POST":
        uname=request.POST['username']
        pwd=request.POST['password']
        #user=auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        user=auth.authenticate(username=uname, password=pwd)
        
        if user is not None:
            auth.login(request,user)
            return redirect(show)
        else:
            return render(request, 'home.html',{'error':"Invalid Login Details"})
    else:
        return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        #create the user if the method is post
        if request.POST['password'] == request.POST['passwordagain']:
            #both pssword are same
            try:
                user= User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', {'error':"Username Match ie you are there already"})
            except User.DoesNotExist:
                user= User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
                return redirect(home)
        else:
            return render(request, 'register.html', {'error':"Password Dont Match"})
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect(home)