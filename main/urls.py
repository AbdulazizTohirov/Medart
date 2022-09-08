from django.urls import path
from .views import *

urlpatterns = [
    path ('', Info_List_view, name='home')
 ]