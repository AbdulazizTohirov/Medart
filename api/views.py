from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from main.models import *
from .serialazers import *

# Info Api View
class InfoListApiView(ListAPIView):
    queryset = InfoModel.objects.all()
    serializer_class = Infoserializer

# Our Services Api View
class OurServicesListApiView(ListAPIView):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer

# Link Api View
class LinkListApiView(ListAPIView):
    queryset = LinkModel.objects.all()
    serializer_class = LinkSerializer

# Contact Api View
class ContactListApiView(CreateAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactSerializer

# About Us Block Api View
class AboutusblockListApiView(ListAPIView):
    queryset = AboutusblockModel.objects.all()
    serializer_class = Aboutus_blogSerializer

# Doctors Api View
class DoctorsListApiView(ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer

# Operationg Attented Api View
class OperationgAttentedsListApiView(ListAPIView):
    queryset = Operationg_Attented.objects.all()
    serializer_class = Operetion_Attented_Serializer

# Doctors Detail Api View
class DoctorsDetailListApiView(ListAPIView):
    queryset = Doctors_detail.objects.all()
    serializer_class = DoctorsDetailSerializer

# FAQ Api View
class FAQListpiView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

# Testimonials Api View
class TestimonialsListApiView(ListAPIView):
    queryset = Testimonials.objects.all()
    serializer_class = TestimonialsSerializer

# Blog Api View
class BlogListApiView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# News Api View
class NewsListApiView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# OurService Api View
class OurServiceListApiView(ListAPIView):
    queryset = OurService.objects.all()
    serializer_class = OurServicesSerializer

# Introduction Api View
class IntroductionListApiView(ListAPIView):
    queryset = Introduction.objects.all()
    serializer_class = IntroductionSerializer

# Consulting Api View
class ConsultingListApiView(ListAPIView):
    queryset = Consulting.objects.all()
    serializer_class = ConsultingSerializer

# Appointment Api View
class AppointmentListApiView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    serializer_class = ConsultingSerializer

# Aboutus_blog Api View
class Aboutus_blogListApiView(ListAPIView):
    queryset = Aboutus_block.objects.all()
    serializer_class = Aboutus_blogSerializer
