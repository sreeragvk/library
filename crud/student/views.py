from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p1=request.POST['p1']
        p2=request.POST['p2']
        f=request.POST['f']
        l=request.POST['l']
        e=request.POST['e']
        if(p1==p2):
            user=User.objects.create_user(username=u,password=p1,first_name=f,last_name=l,email=e)
            user.save()
        return redirect('library:home')
    return render(request,'register.html')
def user_login(request):
    if(request.method=="POST"):
        u=request.POST['user']
        p=request.POST['pass']
        user=authenticate(username=u,password=p)
        if(user):
            login(request,user)
            return redirect('library:home')
        else:
            messages.error(request,"invalid")
    return render(request,'login.html')
def user_logout(request):
    logout(request)
    return user_login(request)

