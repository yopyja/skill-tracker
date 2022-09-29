from django.urls import path
from api import views

urlpatterns = [

    path('teams/', views.TeamApi),
    path('teams/<int:id>', views.TeamApi),

    path('orgs/', views.OrganizationApi),
    path('orgs/<int:id>', views.OrganizationApi),

    path('roles/', views.RolesApi),
    path('roles/<int:id>', views.RolesApi),
    
    path('api/<int:id>', views.Sub_PermissionsApi),

    path('api/<int:id>', views.Granted_PermissionsApi),

    path('users/', views.UserApi, name='allUser'),
    path('users/<int:id>', views.UserApi),

    path('api/<int:id>', views.Skill_LevelApi),

    path('api/<int:id>', views.SkillApi),

    path('api/<int:id>', views.Skill_GroupApi),

    path('api/<int:id>', views.Sub_Rating_TypesApi),

    path('team/<int:id>', views.LoggingApi),

    path('team/<int:id>', views.Assoc_User_SkillsApi),

    path('team/<int:id>', views.Assoc_User_TeamsApi),

    path('team/<int:id>', views.Assoc_User_SkillsApi),

    path('user_team_skill/', views.UserTeamSkill, name='user_team_skill'),
    path('user_team_skill/<int:id>', views.UserTeamSkill),
]