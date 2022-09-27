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

    path("team_management_dashboard/", views.all_teams, name="team_management_dashboard"),
    
    # path("team_management_dashboard/", views.add_team, name="team_management_dashboard"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("edit_user/", views.edit_user, name="edit_user"),
    
]