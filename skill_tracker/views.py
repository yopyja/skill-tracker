from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    my_dict = {'insert_content':"skill_tracker app view"}
    return render(request, 'skill_tracker/index.html', context=my_dict)