from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from main.models import *
from .serializers import *
from rest_framework.response import Response
# Info Api View
class InfoListApiView(ListAPIView):
    queryset = InfoModel.objects.all()
    serializer_class = Infoserializer

# Our Services Api View
class OurServicesListApiView(ListAPIView):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer


# Doctors Api View
class DoctorsListApiView(ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer

# Operationg Attented Api View
class OperationgAttentedsListApiView(ListAPIView):
    queryset = Operationg_Attented.objects.all()
    serializer_class = Operetion_Attented_Serializer

# Operationg Attented RetriveApi View
class OperationgAttentedsRetriveApiView(RetrieveAPIView):
    queryset = Operationg_Attented.objects.all()
    serializer_class = Operetion_Attented_Serializer

# Doctors About Api View
class DoctorsAboutListApiView(ListAPIView):
    queryset = Doctors_about.objects.all()
    serializer_class = DoctorsAboutSerializer

# Doctors About Api View
class DoctorsAboutRetriveApiView(RetrieveAPIView):
    queryset = Doctors_about.objects.all()
    serializer_class = DoctorsAboutSerializer

# FAQ Api View
class FAQListpiView(RetrieveAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get(self, request, pk):
        query = FAQ.objects.filter(status=pk)
        ser = self.serializer_class(query, many=True)
        return Response(ser.data)

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

# Aboutus_blog Api View
class Aboutus_blogListApiView(ListAPIView):
    queryset = Aboutus_block.objects.all()
    serializer_class = Aboutus_blogSerializer
