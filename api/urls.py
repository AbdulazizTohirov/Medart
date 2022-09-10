from django.urls import path
from .views import *
urlpatterns = [
    # Info Urls
    path('info/', InfoListApiView.as_view()),

    # Our Services Url
    path('ourservices/', OurServicesListApiView.as_view()),

     # Doctors Url
    path('doctors/', DoctorsListApiView.as_view()),

     # Operationg Attenteds Url
    path('operation/attenteds/', OperationgAttentedsListApiView.as_view()),
    path('operation/detail/<int:pk>/', OperationgAttentedsRetriveApiView.as_view()),

     # Doctors Detail Url
    path('doctors/about/', DoctorsAboutListApiView.as_view()),
    path('doctors/detail/<int:pk>/', DoctorsAboutRetriveApiView.as_view()),

     # FAQ Url
    path('faq/<int:pk>/', FAQListpiView.as_view()),

     # Testimonials Url
    path('testimonial/',TestimonialsListApiView.as_view()),

     # BlogList Url
    path('blog/',BlogListApiView.as_view()),

     # News Url
    path('news/',NewsListApiView.as_view()),

     # Introduction Url
    path('introduction/',IntroductionListApiView.as_view()),

     # Consulting Url
    path('consulting/',ConsultingListApiView.as_view()),

     # Appointment Url
    path('appointment/',AppointmentListApiView.as_view()),

     # Aboutus_blog Url
    path('about-us-blog/',Aboutus_blogListApiView.as_view()),
]
