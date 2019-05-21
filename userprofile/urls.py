from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    path('login/', views.user_login, name='user-login'),
    path('logout/', views.user_logout, name='user-logout'),
    path('register/', views.user_register, name='user-register'),
    path('delete/<int:id>/', views.user_delete, name='user-delete'),
]
