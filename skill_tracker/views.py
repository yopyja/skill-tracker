from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from skill_tracker.models import *
from skill_tracker.serializers import *

# Create your views here.
def index(request):
    my_dict = {'insert_content':"skill_tracker app view"}
    return render(request, 'skill_tracker/index.html', context=my_dict)

@csrf_exempt
def TeamApi(request, id=0):
    if request.method=='GET':
        team = Team.objects.all()
        team_serializer = TeamSerializer(team,many=True)
        return JsonResponse(team_serializer.data, safe=False)
    elif request.method=='POST':
        team_data=JSONParser().parse(request)
        team_serializer=TeamSerializer(data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    