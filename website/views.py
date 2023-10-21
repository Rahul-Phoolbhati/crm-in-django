from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Record  # Importing th model
from .forms import SignUpForm,AddRecord


def home(request):

    Recordss=Record.objects.all()# Retrieve all user objects
    return render(request, 'home.html', {'Recordss': Recordss})

     # check to dee login
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"] #password in bracket beacuse we gave name="password" in form
        user = authenticate(request, username=username, password=password)

        if user is not None: # succesfull login
            login(request,user)  #login now 
            messages.success(request,"u have beeeeeen logged succesfully")
            return redirect('homee')
        else:
            messages.success(request,"Try Again")

    return render (request,'home.html',{'Recordss':Recordss})

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

def customer(request,pk):
    if request.user.is_authenticated:

        #see teh recordss
        customer=Record.objects.get(id=pk)
        return render(request,'record.html',{'customer':customer})
    else:
        messages.success(request,"You can't edit, as u must be logij to view that page ")
        return redirect(request,'homee')

def delete__(request,pk):
    if request.user.is_authenticated:

        delete_=Record.objects.get(id=pk)
        delete_.delete()
        messages.success(request,"Record deleeted ")
        return redirect('homee')
    else:
        messages.success(request,"You can't edit, as u must be logij to view that page ")
        return redirect('homee')

def add(request):
    forrm = AddRecord(request.POST or None)  
    if request.user.is_authenticated:
        if request.method=="POST":
            if forrm.is_valid():
                add_=forrm.save()
                messages.success(request, "Record added successfully")
                return redirect('homee')

        return render(request, 'add_record.html', {'forrm': forrm})
    else:
        messages.success(request, "You can't add a record as you must be logged in to view that page")
        return redirect('homee')
        
def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecord(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('homee')
		return render(request, 'update_record.html', {'form':form})
	else: 
		messages.success(request, "You Must Be Logged In...")
		return redirect('homee')


     