from django.urls import path
from . import views

urlpatterns = [
    path('',views.members,name='main'),
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('test/', views.test, name='test'),
    path('userprofile/', views.userprofile, name='userprofile'),
]