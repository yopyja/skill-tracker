from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Departments(models.Model):
    testing = models.AutoField

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    logo = models.BinaryField(null=True)

class Organization(models.Model):
    org = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    logo = models.BinaryField(null=True)

class Roles(models.Model):
    role = models.AutoField(primary_key=True)
    org = models.ForeignKey(Organization, on_delete=models.PROTECT)
    is_team = models.BooleanField()

# class Sub_Permissions(models.Model):
#     sub_permission_id = models.AutoField(primary_key=True)
#     description = models.CharField(max_length=300)

# class Granted_Permissions(models.Model):
#     granted_permissions_id = models.AutoField(primary_key=True)
#     is_user = models.BooleanField()
#     sub_permissions_id = models.ForeignKey(Sub_Permissions, on_delete=models.CASCADE)
#     entity_id = models.IntegerField()

# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     prefix = models.CharField(max_length=5)
#     position = models.CharField(max_length=50)
#     archived = models.BooleanField(null=False, default=False)

class Skill_Level(models.Model):
    skill_level = models.AutoField(primary_key=True)
    rating_type = models.IntegerField
    rating_value = models.CharField(max_length=50)

class Skill(models.Model):
    skill = models.AutoField(primary_key=True)
    skill_label = models.CharField(max_length=75)
    archived = models.BooleanField(null=False)
    
class Skill_Group(models.Model):
    skill_group = models.AutoField(primary_key=True)
    group_label = models.CharField(max_length=75)
    
class Sub_Rating_Types(models.Model):
    rating_type = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)

class Logging(models.Model):
    log = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, null=True, on_delete=models.PROTECT)
    in_training = models.BooleanField(null=True)
    date = models.DateTimeField
    action = models.CharField(max_length=75)
    
class Assoc_User_Skills(models.Model):
    user_skill = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    skill_level = models.ForeignKey(Skill_Level, on_delete=models.CASCADE)

class Assoc_User_Teams(models.Model):
    team_user = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    
class Assoc_Group_Skills(models.Model):
    group_skill = models.AutoField(primary_key=True)
    skill_group = models.ForeignKey(Skill_Group, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)


