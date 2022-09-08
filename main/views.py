from django.shortcuts import render
from .models import *
from django.views.generic import ListView

def Info_List_view(ListView):
    info = InfoModel
    template_name = 'index.html' 