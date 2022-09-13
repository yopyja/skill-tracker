from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    my_dict = {'insert_me':"logging app view"}
    return render(request, 'api/index.html', context=my_dict)