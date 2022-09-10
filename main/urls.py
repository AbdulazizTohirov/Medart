from django.urls import path
from .views import *

urlpatterns = [
    path ('', info_list_view, name='home')
 ]