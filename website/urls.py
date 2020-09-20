from django.urls import path

from . import views
from website.views import home

urlpatterns = [
    path('', views.home, name='home'),
   
]
