from django.urls import path
from api import views

urlpatterns = [
    path('api/', views.TeamApi), 
    
    path('api/<int:id>', views.TeamApi),

    path('api/<int:id>', views.OrganizationApi),

    path('api/<int:id>', views.RolesApi),
    
    path('api/<int:id>', views.Sub_PermissionsApi),

    path('api/<int:id>', views.Granted_PermissionsApi),

    path('api/<int:id>', views.UserApi),

    path('api/<int:id>', views.Skill_LevelApi),

    path('api/<int:id>', views.SkillApi),

    path('api/<int:id>', views.Skill_GroupApi),

    path('api/<int:id>', views.Sub_Rating_TypesApi),

    path('team/<int:id>', views.LoggingApi),

    path('team/<int:id>', views.Assoc_User_SkillsApi),

    path('team/<int:id>', views.Assoc_User_TeamsApi),

    path('team/<int:id>', views.Assoc_User_SkillsApi),
]