from django.urls import path
from .views import *

urlpatterns = [ 
    path('news/', NewsView.as_view()),     
 ]