from django.urls import path
from .views import *
urlpatterns = [
    # Info Urls
    path('api/',InfoListApiView.as_view()),

    # Our Services Url
    path('api/',OurServicesListApiView.as_view()),

    # Link Url Url
    path('api/',LinkListApiView.as_view()),

    # Contact Url
    path('api/',ContactListApiView.as_view()),

     # About Us Block Url
    path('api/',AboutusblockListApiView.as_view()),

     # Doctors Url
    path('api/',DoctorsListApiView.as_view()),

     # Operationg Attenteds Url
    path('api/',OperationgAttentedsListApiView.as_view()),

     # Doctors Detail Url
    path('api/',DoctorsDetailListApiView.as_view()),

     # FAQ Url
    path('api/',FAQListpiView.as_view()),

     # Testimonials Url
    path('api/',TestimonialsListApiView.as_view()),

     # BlogList Url
    path('api/',BlogListApiView.as_view()),

     # News Url
    path('api/',NewsListApiView.as_view()),

     # Our Service Url
    path('api/',OurServiceListApiView.as_view()),

     # Introduction Url
    path('api/',IntroductionListApiView.as_view()),

     # Consulting Url
    path('api/',ConsultingListApiView.as_view()),

     # Our Services Url
    path('api/',AppointmentListApiView.as_view()),

     # Our Services Url
    path('api/',Aboutus_blogListApiView.as_view()),
]
