from django.urls import path
from .views import *
urlpatterns = [
    # Info Urls
    path('Info/list',InfoListApiView.as_view()),

    # Our Services Url
    path('ourservices/list',OurServicesListApiView.as_view()),

    # Link Url Url
    path('link/list',LinkListApiView.as_view()),

    # Contact Url
    path('contact/list',ContactListApiView.as_view()),

     # About Us Block Url
    path('about/us/block/list',AboutusblockListApiView.as_view()),

     # Doctors Url
    path('doctors/list',DoctorsListApiView.as_view()),

     # Operationg Attenteds Url
    path('operation/attenteds/list',OperationgAttentedsListApiView.as_view()),

     # Doctors Detail Url
    path('doctorr/detail/list',DoctorsDetailListApiView.as_view()),

     # FAQ Url
    path('faq/list',FAQListpiView.as_view()),

     # Testimonials Url
    path('testimonial/list',TestimonialsListApiView.as_view()),

     # BlogList Url
    path('blog/list',BlogListApiView.as_view()),

     # News Url
    path('news/list',NewsListApiView.as_view()),

     # Our Service Url
    path('our/service/list',OurServiceListApiView.as_view()),

     # Introduction Url
    path('introduction/list',IntroductionListApiView.as_view()),

     # Consulting Url
    path('consulting/list',ConsultingListApiView.as_view()),

     # Our Services Url
    path('appointment/list',AppointmentListApiView.as_view()),

     # Our Services Url
    path('about/us/blo',Aboutus_blogListApiView.as_view()),
]
