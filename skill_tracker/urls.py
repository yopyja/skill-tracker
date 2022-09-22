"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from skill_tracker import views

urlpatterns = [
    path("register/", views.register_request, name="register"),

    path('', views.index, name='index'), 

    path("edit_user/", views.edit_user, name="edit_user"),

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