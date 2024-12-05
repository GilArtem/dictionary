from django.urls import path
from . import views

urlpatterns = [
    path('', views.polls_home_page, name='polls_home_page'),
    
]
