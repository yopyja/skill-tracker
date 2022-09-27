from django.urls import path
from SiteManagement import views

urlpatterns = [
    path("register/", views.register_request, name="register"),

    path('user_login/', views.user_login, name='user_login'),

    path('logout_user', views.logout_user, name='user_logout'),
    
]