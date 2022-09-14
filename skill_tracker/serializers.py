from dataclasses import fields
from rest_framework import serializers
from skill_tracker.models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=('team_id','name','description','is_active','logo')

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields=('orgi_id','name','logo')