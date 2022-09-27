from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from .forms import AddTeamForm, EditUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from api.models import *

# Create your views here.
# def login_user(request):
#     form = 
#     return render(request=request, template_name="authenticate/login.html", context={"user_login_form":form})


def index(request):
    my_dict = {'insert_content':"skill_tracker app view"}
    return render(request, 'skill_tracker/index.html', context=my_dict)

def edit_user(request):
        form = EditUserForm(data=request.POST or None, instance=request.user)        
        if form.is_valid():
            user = form.save()
            messages.success(request, "User Edit successful." )
            return redirect("edit_user")    
        return render(request, 'skill_tracker/edit_user.html', {'edit_user':form})


def dashboard(request):
    return render(request, 'skill_tracker/dashboard.html', {})

def team_management(request):
    _all_teams = all_teams(request)
    _add_team = add_team(request)
    context = {
        'team_list' : _all_teams,
        'add_team': _add_team,
    }
    if request.method=='POST':
        _add_team.save()
        messages.success(request, "Team Successfully Added")
        return redirect('team_management_dashboard')
    return render(request, 'skill_tracker/team_management_dashboard.html', context)

def all_teams(request):
    team_list = Team.objects.all()
    # return render(request, 'skill_tracker/team_management_dashboard.html', {'team_list':team_list})
    return team_list

def add_team(request):
    add_team = AddTeamForm(request.POST or None)
    # if request.method=='POST':
    #     add_team.save()
    #     messages.success(request, "Team Successfully Added")
    #     return redirect('team_management_dashboard')
    # return render (request, 'skill_tracker/team_management_dashboard.html', {'add_team':add_team})
    return add_team
