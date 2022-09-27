from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from .forms import NewUserForm, EditUserForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from skill_tracker.models import *

# Create your views here.
# def login_user(request):
#     form = 
#     return render(request=request, template_name="authenticate/login.html", context={"user_login_form":form})


def index(request):
    my_dict = {'insert_content':"skill_tracker app view"}
    return render(request, 'skill_tracker/index.html', context=my_dict)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("dashboard")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="authenticate/register.html", context={"register_form":form})

def edit_user(request):
    if request.method=='POST':
        form = EditUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Edit successful." )
            return redirect("index")
    form = EditUserForm()
    return render (request, 'skill_tracker/edit_user.html', {'user_form':form})

def user_login(request):
    form = UserLoginForm(request.POST or None)
    context = {'user_login':form}
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("There was an error loggin in. Try again."))
            return redirect('user_login')        
    else:
        return render(request, 'authenticate/login.html', context)
        
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out."))
    return redirect('user_login')

def dashboard(request):
    return render(request, 'skill_tracker/dashboard.html', {})

