from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from .forms import NewUserForm, EditUserForm, UserLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

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
