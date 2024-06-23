from django.urls import path
from .views import *



urlpatterns = [
    path('index/', index, name='index'),
    path('signin/', signin, name='signin'),
    path('dash/', dash, name='dash'),
    
]

