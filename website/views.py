from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .forms import SignUpForm

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
    if request.method=='POST':   
        form=SignUpForm(request.POST)
        if form.is_valid():

            form.save()

            #auhenticae & logging
            username = form.cleaned_data['username'] #username = ...  assigns the cleaned 'username' value to the username variable. 
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,"You have Succesfully Registered")
            return redirect(request,'homee')

    else:                  #when  no action of POST
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})# passes the "form":form  as context data to the template,html

    return render(request,'register.html', {'form': form})
