from pydoc import describe
from pyexpat import model
from django.db import models

# Create your models here.
class Departments(models.Model):
    testing = models.AutoField

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    is_active = models.BooleanField()
    logo = models.BinaryField(null=True)

class Organization(models.Model):
    org_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    logo = models.BinaryField(null=True)

class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    org_id = models.ForeignKey(Organization.org_id, on_delete=models.PROTECT)
    is_team = models.BooleanField()

class Sub_Permissions(models.Model):
    sub_permission_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300)

class Granted_Permissions(models.Model):
    granted_permissions_id = models.AutoField(primary_key=True)
    is_user = models.BooleanField()
    sub_permissions_id = models.ForeignKey(Sub_Permissions.sub_permissions_id, on_delete=models.CASCADE)
    entity_id = models.IntegerField()

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    prefix = models.CharField(max_length=5)
    position = models.CharField(max_length=50)
    archived = models.BooleanField(null=False)

class Skill_Level(models.Model):
    skill_level_id = models.AutoField(primary_key=True)
    rating_type = models.IntegerField
    rating_value = models.CharField(max_length=50)

class Skill(models.Model):
    skill_id = models.AutoField(primary_key=True)
    skill_label = models.CharField(max_length=75)
    archived = models.BooleanField(null=False)
    
class Skill_Group(models.Model):
    skill_group_id = models.AutoField(primary_key=True)
    group_label = models.CharField(max_length=75)
    
class Sub_Rating_Types(models.Model):
    rating_type_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)

class Logging(models.Model):
    logging_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User.user_id, null=True, on_delete=models.PROTECT)
    skill_id = models.ForeignKey(Skill.skill_id, null=True, on_delete=models.PROTECT)
    in_training = models.BooleanField(null=True)
    date = models.DateTimeField
    action = models.CharField(max_length=75)
    
class Assoc_User_Skills(models.Model):
    user_skill_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User.user_id, on_delete=models.PROTECT)
    skill_level_id = models.ForeignKey(Skill_Level.skill_level_id, on_delete=models.CASCADE)

class Assoc_User_Teams(models.Model):
    team_user_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User.user_id, on_delete=models.PROTECT)
    team_id = models.ForeignKey(Team.team_id, on_delete=models.CASCADE)
    
class Assoc_Group_Skills(models.Model):
    group_skill_id = models.AutoField(primary_key=True)
    skill_group_id = models.ForeignKey(Skill_Group.skill_group_id, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill.skill_id)
