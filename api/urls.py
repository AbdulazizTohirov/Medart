from django.urls import path
from .views import *

urlpatterns = [
    path('info/', InfoView.as_view()),
    path('ourservices/', OurServicesView.as_view()),
    path('doctors/', DoctorsView.as_view()),
    path('doctors/count/', DoctorsCountView),
    path('doctors/detail/<int:doctor>/', DoctorsDetailView.as_view()),
    path('faq/<int:faq>/', FAQView.as_view()),
    path('testimonial/', TestimonialsView.as_view()),
    path('blog/', BlogView.as_view()),
    path('news/', NewsView.as_view()),
    path('news/filter/<int:news>/', NewsFilterView.as_view()),
    path('consulting/', ConsultingView.as_view()),
    path('appointment/', AppointmentView.as_view()),
    path('aboutusblog/', Aboutus_blogView.as_view()),

    # path('ourservices/filter_banner/', OurServicesFilterBannerView.as_view()),
    # path('blog/detail/<int:detail>/', BlogDetailView.as_view()),
    # path('introduction/', IntroductionView.as_view()),

]
