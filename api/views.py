from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView
from main.models import *
from .serializers import *
from rest_framework.response import Response
# Info Api View
class InfoView(ListAPIView):
    queryset = InfoModel.objects.all()
    serializer_class = Infoserializer

# Our Services Api View
class OurServiseView(ListAPIView):
    queryset = OurService.objects.filter(banner=True).order_by('-id')
    serializer_class = OurServiceSerializer


# Doctors Api View
class DoctorsView(ListAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorsSerializer

# Operationg Attented Api View
class OperationgAttentedsView(ListAPIView):
    queryset = Operationg_Attented.objects.all()
    serializer_class = Operetion_Attented_Serializer

# Operationg Attented RetriveApi View
class OperationgAttentedsRetriveApiView(RetrieveAPIView):
    queryset = Operationg_Attented.objects.all()
    serializer_class = Operetion_Attented_Serializer

# Doctors Count 
@api_view(['GET'])
def doctors_count(request):
    doctors_quantity = Doctors.objects.all().count()
    data = {
        'success':True,
        'qunatity_doctor':doctors_quantity
    }
    return Response(data)

# Doctors About Api View
class DoctorsAboutListApiView(ListAPIView):
    queryset = Doctors_about.objects.all()
    serializer_class = DoctorsAboutSerializer

# Doctors About Api View
class DoctorsAboutRetriveApiView(RetrieveAPIView):
    queryset = Doctors_about.objects.all()
    serializer_class = DoctorsAboutSerializer

# FAQ Api View
class FAQListpiView(ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    
    def get(self, request, pk):
        query = FAQ.objects.filter(status=pk)
        return Response(FAQSerializer(query, many=True).data) 

# Testimonials Api View
class TestimonialsView(ListAPIView):
    queryset = Testimonials.objects.all().order_by('id')[:5]
    serializer_class = TestimonialsSerializer

# Blog Api View
class OurBlog(ListAPIView):
    blogs = Blog.objects.all().order_by('-id')[:8]
    serializer = BlogSerializer(blogs, many=True)

#  News Api view 1
# class NewsApiView(RetrieveAPIView):
#     def
# News Api View 2
class NewsView(ListAPIView):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer

# New
class NewaListView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get(self, request, pk):
        query = News.objects.filter(status=pk)
        return Response(NewsSerializer(query, many=True).data)


# Introduction Api View
class IntroductionView(ListAPIView):
    queryset = Introduction.objects.all().order_by('-id')
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
class Aboutus_blogView(ListAPIView):
    queryset = Aboutus_block.objects.all().order_by('-id')[:4]
    serializer_class = Aboutus_blogSerializer
