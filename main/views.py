from django.shortcuts import render
from .models import *
from django.views.generic import ListView

def info_list_view(ListView):
    info = InfoModel
    template_name = 'index.html' 

def our_block(request):
    blogs = Blog.objects.all().order_by('-id')[:8]
    return render(request,'ourblog.html')

def about_us_blog(request):
    blogs = Aboutus_block.objects.all().order_by('-id')[:4]
    return render(request,'about-us.html')

def testimonial_view(reques):
    testimonials = Testimonials.objects.all().order_by('id')[:5]