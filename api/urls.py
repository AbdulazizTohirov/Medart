from django.urls import path
from .views import *
from main.views import *
urlpatterns = [
    # Info Urls
    path('info/', InfoView.as_view()),

    # Our Services Url
    path('ourservices/', OurServiseView.as_view()),
    path('doctors/count/', doctors_count),
     # Doctors Url
    path('doctors/', DoctorsView.as_view()),

     # Operationg Attenteds Url
    path('operation/attenteds/', OperationgAttentedsView.as_view()),
    path('operation/detail/<int:pk>/', OperationgAttentedsRetriveApiView.as_view()),

     # Doctors Detail Url
    path('doctors/about/', DoctorsAboutListApiView.as_view()),
    path('doctors/detail/<int:pk>/', DoctorsAboutRetriveApiView.as_view()),

     # FAQ Url
    path('faq/<int:pk>/', FAQListpiView .as_view()),

     # Testimonials Url
    path('testimonial/',TestimonialsView.as_view()),

     # BlogList Url
    path('blog/',OurBlog.as_view()),

     # News Url
    path('news/',NewsView.as_view()),
    path('news/<int:pk>/',NewaListView.as_view()),

     # Introduction Url
    path('introduction/',IntroductionView.as_view()),

     # Consulting Url
    path('consulting/',ConsultingListApiView.as_view()),

     # Appointment Url
    path('appointment/',AppointmentListApiView.as_view()),

     # Aboutus_blog Url
    path('about-us-blog/',Aboutus_blogView.as_view()),
]
