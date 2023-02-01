from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.Super_admin.as_view(), name='user'),
    path('login/', views.login , name='login'),
    path('branch/', views.Branch.as_view(), name='branch'),
    path('branch_manager/<id>/', views.Asign_branch_man.as_view(),name='branch'),
    path('batch/', views.Batch.as_view(), name= 'batch'),
    path('course/', views.Course.as_view(), name='course'),
    path('subject/', views.Subject.as_view(), name='subject'),
    path('topic/', views.Topic.as_view(), name='topic'),
    path('subtopic/', views.Subtopic.as_view(), name='subtopic'),
    path('facverify/<id>/', views.faculty_verify, name='verify'),
    path('facreject/<id>/', views.faculty_reject, name='reject'),
    path('fac/', views.faculty, name='fac'),
    path('addfac/', views.add_fac, name='addfac')

]