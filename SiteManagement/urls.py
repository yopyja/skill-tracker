from django.urls import path
from SiteManagement import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.register_request, name="register"),

    path('user_login/', views.user_login, name='user_login'),

    path('logout_user', views.logout_user, name='user_logout'),

    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authenticate/password_reset_done.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="authenticate/password_reset_confirm.html"), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authenticate/password_reset_complete.html'), name='password_reset_complete'),
    
    path("password_reset/", views.password_reset_request, name="password_reset")
]