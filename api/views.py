from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from api.models import *
from api.serializers import *


# Create your views here.
def index(request):
    my_dict = {'insert_me':"logging app view"}
    return render(request, 'api/index.html', context=my_dict)

@csrf_exempt
def TeamApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            team = Team.objects.all()
            team_serializer = TeamSerializer(team,many=True)
            return JsonResponse(team_serializer.data, safe=False)
        elif id is not None:
            team = Team.objects.get(team_id=id)
            team_serializer = TeamSerializer(team)
            return JsonResponse(team_serializer.data, safe=False)
    elif request.method=='POST':
        team_data=JSONParser().parse(request)
        team_serializer=TeamSerializer(data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        team_data=JSONParser().parse(request)
        team=Team.objects.get(team_id=team_data['team_id'])
        team_serializer=TeamSerializer(team, data=team_data)
        if team_serializer.is_valid():
            team_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)
    
@csrf_exempt
def OrganizationApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            organization = Organization.objects.all()
            organization_serializer = OrganizationSerializer(organization,many=True)
            return JsonResponse(organization_serializer.data, safe=False)
        elif id is not None:
            organization = Organization.objects.get(organization_id=id)
            organization_serializer = OrganizationSerializer(organization)
            return JsonResponse(organization_serializer.data, safe=False)
    elif request.method=='POST':
        organization_data=JSONParser().parse(request)
        organization_serializer=OrganizationSerializer(data=organization_data)
        if organization_serializer.is_valid():
            organization_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        organization_data=JSONParser().parse(request)
        organization=Organization.objects.get(organization_id=organization_data['organization_id'])
        organization_serializer=OrganizationSerializer(organization, data=organization_data)
        if organization_serializer.is_valid():
            organization_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def RolesApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            roles = Roles.objects.all()
            roles_serializer = RolesSerializer(roles,many=True)
            return JsonResponse(roles_serializer.data, safe=False)
        elif id is not None:
            roles = Roles.objects.get(roles_id=id)
            roles_serializer = RolesSerializer(roles)
            return JsonResponse(roles_serializer.data, safe=False)
    elif request.method=='POST':
        roles_data=JSONParser().parse(request)
        roles_serializer=RolesSerializer(data=roles_data)
        if roles_serializer.is_valid():
            roles_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        roles_data=JSONParser().parse(request)
        roles=Roles.objects.get(roles_id=roles_data['roles_id'])
        roles_serializer=RolesSerializer(roles, data=roles_data)
        if roles_serializer.is_valid():
            roles_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def Sub_PermissionsApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            sub_permissions = Sub_Permissions.objects.all()
            sub_permissions_serializer = Sub_PermissionsSerializer(sub_permissions,many=True)
            return JsonResponse(sub_permissions_serializer.data, safe=False)
        elif id is not None:
            sub_permissions = Sub_Permissions.objects.get(sub_permissions_id=id)
            sub_permissions_serializer = Sub_PermissionsSerializer(sub_permissions)
            return JsonResponse(sub_permissions_serializer.data, safe=False)
    elif request.method=='POST':
        sub_permissions_data=JSONParser().parse(request)
        sub_permissions_serializer=Sub_PermissionsSerializer(data=sub_permissions_data)
        if sub_permissions_serializer.is_valid():
            sub_permissions_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        sub_permissions_data=JSONParser().parse(request)
        sub_permissions=Sub_Permissions.objects.get(sub_permissions_id=sub_permissions_data['sub_permissions_id'])
        sub_permissions_serializer=Sub_PermissionsSerializer(sub_permissions, data=sub_permissions_data)
        if sub_permissions_serializer.is_valid():
            sub_permissions_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def Granted_PermissionsApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            granted_permissions = Granted_Permissions.objects.all()
            granted_permissions_serializer = Granted_PermissionsSerializer(granted_permissions,many=True)
            return JsonResponse(granted_permissions_serializer.data, safe=False)
        elif id is not None:
            granted_permissions = Granted_Permissions.objects.get(granted_permissions_id=id)
            granted_permissions_serializer = Granted_PermissionsSerializer(granted_permissions)
            return JsonResponse(granted_permissions_serializer.data, safe=False)
    elif request.method=='POST':
        granted_permissions_data=JSONParser().parse(request)
        granted_permissions_serializer=Granted_PermissionsSerializer(data=granted_permissions_data)
        if granted_permissions_serializer.is_valid():
            granted_permissions_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        granted_permissions_data=JSONParser().parse(request)
        granted_permissions=Granted_Permissions.objects.get(granted_permissions_id=granted_permissions_data['granted_permissions_id'])
        granted_permissions_serializer=Granted_PermissionsSerializer(granted_permissions, data=granted_permissions_data)
        if granted_permissions_serializer.is_valid():
            granted_permissions_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def UserApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            user = User.objects.all()
            user_serializer = UserSerializer(user,many=True)
            return JsonResponse(user_serializer.data, safe=False)
        elif id is not None:
            user = User.objects.get(user_id=id)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data, safe=False)
    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        user_data=JSONParser().parse(request)
        user=User.objects.get(user_id=user_data['user_id'])
        user_serializer=UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def Skill_LevelApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            skill_level = Skill_Level.objects.all()
            skill_level_serializer = Skill_LevelSerializer(skill_level,many=True)
            return JsonResponse(skill_level_serializer.data, safe=False)
        elif id is not None:
            skill_level = Skill_Level.objects.get(skill_level_id=id)
            skill_level_serializer = Skill_LevelSerializer(skill_level)
            return JsonResponse(skill_level_serializer.data, safe=False)
    elif request.method=='POST':
        skill_level_data=JSONParser().parse(request)
        skill_level_serializer=Skill_LevelSerializer(data=skill_level_data)
        if skill_level_serializer.is_valid():
            skill_level_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        skill_level_data=JSONParser().parse(request)
        skill_level=Skill_Level.objects.get(skill_level_id=skill_level_data['skill_level_id'])
        skill_level_serializer=Skill_LevelSerializer(skill_level, data=skill_level_data)
        if skill_level_serializer.is_valid():
            skill_level_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def SkillApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            skill = Skill.objects.all()
            skill_serializer = SkillSerializer(skill,many=True)
            return JsonResponse(skill_serializer.data, safe=False)
        elif id is not None:
            skill = Skill.objects.get(skill_id=id)
            skill_serializer = SkillSerializer(skill)
            return JsonResponse(skill_serializer.data, safe=False)
    elif request.method=='POST':
        skill_data=JSONParser().parse(request)
        skill_serializer=SkillSerializer(data=skill_data)
        if skill_serializer.is_valid():
            skill_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        skill_data=JSONParser().parse(request)
        skill=Skill.objects.get(skill_id=skill_data['skill_id'])
        skill_serializer=SkillSerializer(skill, data=skill_data)
        if skill_serializer.is_valid():
            skill_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def Skill_GroupApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            skill_group = Skill_Group.all()
            skill_group_serializer = Skill_GroupSerializer(skill_group,many=True)
            return JsonResponse(skill_group_serializer.data, safe=False)
        elif id is not None:
            skill_group = Skill_Group.get(skill_group_id=id)
            skill_group_serializer = Skill_GroupSerializer(skill_group)
            return JsonResponse(skill_group_serializer.data, safe=False)
    elif request.method=='POST':
        skill_group_data=JSONParser().parse(request)
        skill_group_serializer=Skill_GroupSerializer(data=skill_group_data)
        if skill_group_serializer.is_valid():
            skill_group_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        skill_group_data=JSONParser().parse(request)
        skill_group=Skill_Group.get(skill_group_id=skill_group_data['skill_group_id'])
        skill_group_serializer=Skill_GroupSerializer(skill_group, data=skill_group_data)
        if skill_group_serializer.is_valid():
            skill_group_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def Sub_Rating_TypesApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            sub_rating_type = Sub_Rating_Types.all()
            sub_rating_type_serializer = Sub_Rating_TypesSerializer(sub_rating_type,many=True)
            return JsonResponse(sub_rating_type_serializer.data, safe=False)
        elif id is not None:
            sub_rating_type = Sub_Rating_Types.get(sub_rating_type_id=id)
            sub_rating_type_serializer = Sub_Rating_TypesSerializer(sub_rating_type)
            return JsonResponse(sub_rating_type_serializer.data, safe=False)
    elif request.method=='POST':
        sub_rating_data=JSONParser().parse(request)
        sub_rating_type_serializer=Sub_Rating_TypesSerializer(data=sub_rating_data)
        if sub_rating_type_serializer.is_valid():
            sub_rating_type_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        sub_rating_data=JSONParser().parse(request)
        sub_rating_type=Sub_Rating_Types.get(sub_rating_type_id=sub_rating_data['sub_rating_type_id'])
        sub_rating_type_serializer=Sub_Rating_TypesSerializer(sub_rating_type, data=sub_rating_data)
        if sub_rating_type_serializer.is_valid():
            sub_rating_type_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def LoggingApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            logging = Logging.all()
            logging_serializer = LoggingSerializer(logging,many=True)
            return JsonResponse(logging_serializer.data, safe=False)
        elif id is not None:
            logging = Logging.get(logging_id=id)
            logging_serializer = LoggingSerializer(logging)
            return JsonResponse(logging_serializer.data, safe=False)
    elif request.method=='POST':
        logging_data=JSONParser().parse(request)
        logging_serializer=LoggingSerializer(data=logging_data)
        if logging_serializer.is_valid():
            logging_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        logging_data=JSONParser().parse(request)
        logging=Logging.get(logging_id=logging_data['logging_id'])
        logging_serializer=LoggingSerializer(logging, data=logging_data)
        if logging_serializer.is_valid():
            logging_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def Assoc_User_SkillsApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            logging = Assoc_User_Skills.all()
            logging_serializer = Assoc_User_SkillsSerializer(logging,many=True)
            return JsonResponse(logging_serializer.data, safe=False)
        elif id is not None:
            logging = Assoc_User_Skills.get(logging_id=id)
            logging_serializer = Assoc_User_SkillsSerializer(logging)
            return JsonResponse(logging_serializer.data, safe=False)
    elif request.method=='POST':
        logging_data=JSONParser().parse(request)
        logging_serializer=Assoc_User_SkillsSerializer(data=logging_data)
        if logging_serializer.is_valid():
            logging_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        logging_data=JSONParser().parse(request)
        logging=Assoc_User_Skills.get(logging_id=logging_data['logging_id'])
        logging_serializer=Assoc_User_SkillsSerializer(logging, data=logging_data)
        if logging_serializer.is_valid():
            logging_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def Assoc_User_TeamsApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            assoc_user_teams_type = Assoc_User_Teams.all()
            assoc_user_teams_type_serializer = Assoc_User_TeamsSerializer(assoc_user_teams_type,many=True)
            return JsonResponse(assoc_user_teams_type_serializer.data, safe=False)
        elif id is not None:
            assoc_user_teams_type = Assoc_User_Teams.get(team_user_id=id)
            assoc_user_teams_type_serializer = Assoc_User_TeamsSerializer(assoc_user_teams_type)
            return JsonResponse(assoc_user_teams_type_serializer.data, safe=False)
    elif request.method=='POST':
        assoc_user_teams_data=JSONParser().parse(request)
        assoc_user_teams_type_serializer=Assoc_User_TeamsSerializer(data=assoc_user_teams_data)
        if assoc_user_teams_type_serializer.is_valid():
            assoc_user_teams_type_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        assoc_user_teams_data=JSONParser().parse(request)
        assoc_user_teams_type=Assoc_User_Teams.get(team_user_id=assoc_user_teams_data['team_user_id'])
        assoc_user_teams_type_serializer=Assoc_User_TeamsSerializer(assoc_user_teams_type, data=assoc_user_teams_data)
        if assoc_user_teams_type_serializer.is_valid():
            assoc_user_teams_type_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)

@csrf_exempt
def Assoc_Group_SkillsApi(request, id=None):
    if request.method=='GET':
        if id is None:            
            assoc_group_skills = Assoc_Group_Skills.all()
            assoc_group_skills_serializer = Assoc_Group_SkillsSerializer(assoc_group_skills,many=True)
            return JsonResponse(assoc_group_skills_serializer.data, safe=False)
        elif id is not None:
            assoc_group_skills = Assoc_Group_Skills.get(group_skill_id=id)
            assoc_group_skills_serializer = Assoc_Group_SkillsSerializer(assoc_group_skills)
            return JsonResponse(assoc_group_skills_serializer.data, safe=False)
    elif request.method=='POST':
        assoc_group_skills_data=JSONParser().parse(request)
        assoc_group_skills_serializer=Assoc_Group_SkillsSerializer(data=assoc_group_skills_data)
        if assoc_group_skills_serializer.is_valid():
            assoc_group_skills_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method=='PUT':
        assoc_group_skills_data=JSONParser().parse(request)
        assoc_group_skills=Assoc_Group_Skills.get(group_skill_id=assoc_group_skills_data['group_skill_id'])
        assoc_group_skills_serializer=Assoc_Group_SkillsSerializer(assoc_group_skills, data=assoc_group_skills_data)
        if assoc_group_skills_serializer.is_valid():
            assoc_group_skills_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to update",safe=False)