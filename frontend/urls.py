from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('team', views.team, name='team'),
    path('testpage', views.testpage),
]
