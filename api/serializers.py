from dataclasses import fields
from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=('team_id','name','description','is_active','logo')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields=('org_id','name','logo')

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Roles
        fields=('role_id','org_id','is_team')

# class Sub_PermissionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Sub_Permissions
#         fields=('sub_permission_id','description')

# class Granted_PermissionsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Granted_Permissions
#         fields=('granted_permissions_id','is_user','subpermissions_id','entity_id')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email')

class Skill_LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill_Level
        fields=('skill_level_id','rating_type','rating_value')

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields=('skill_id','skill_label','archived')

class Skill_GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill_Group
        fields=('skill_group_id','group_label')

class Sub_Rating_TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sub_Rating_Types
        fields=('rating_type_id','description')

class LoggingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Logging
        fields=('logging_id','user_id','skill_id','in_training','date','action')

class Assoc_User_SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assoc_User_Skills
        fields=('user_skill_id','user_id','skill_level_id')

class Assoc_User_TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assoc_User_Teams
        fields=('username','email','team_user_id','user_id','team_id')

class Assoc_Group_SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Assoc_Group_Skills
        fields=('id','group_skill_id','skill_group_id','skill_id')