from django.urls import path, include
from . import views

urlpatterns = [
    path('user/', views.Faculty.as_view(), name='user'),
    path('login/', views.login , name='login'),
    
]