from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"] #password in bracket beacuse we gave name="password" in form
        user = authenticate(request, username=username, password=password)

        if user is not None: # succesfull login
            login(request,user)  #login now 
            messages.success(request,"u have ben logged succesfully")
            return redirect('homee')
        else:
            messages.success(request,"Try Again")

    return render (request,'home.html')

# def login_(request):
#     pass 

def logout_(request):  
    logout(request)
    messages.success(request,"LOgout done")
    return redirect('homee')


def register_(request):
    return render(request,'register.html')

