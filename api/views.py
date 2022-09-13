from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView


class InfoView(ListAPIView):
    def get(self, request):
        queryset_count = InfoModel.objects.all().count()
        if queryset_count > 0:
            queryset = InfoModel.objects.last()
            serializer = Infoserializer(queryset)
            return Response(serializer.data)
        else:
            data = {
                'success': True,
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class OurServicesView(ListAPIView):
    def get(self, request):
        query_count = OurService.objects.all().count()
        if query_count > 0:
            queryset = OurService.objects.all()
            serializer = OurServiceSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            data = {
                'success': True,
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def DoctorsCountView(request):
    doctors_quantity = Doctors.objects.all().count()
    data = {
        'success': True,
        'doctors_quantity': doctors_quantity
    }
    return Response(data)


class DoctorsView(ListAPIView):
    def get(self, request):
        queryset_count = Doctors.objects.all().count()
        if queryset_count > 0:
            queryset = Doctors.objects.all()
            return Response(DoctorsSerializer(queryset, many=True).data)
        else:
            data = {
                'success': True,
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)


class DoctorsDetailView(ListAPIView):
    def get(self, request, doctor=None):
        queryset_count = Doctors.objects.all().count()
        if queryset_count > 0:
            query = Doctors_about.objects.filter(doctor_id=doctor)
            ser = DoctorsAboutSerializer(query, many=True)
            data = {
                'success': True,
                'queryset': ser.data,
            }
        else:
            data = {
                'success': True,
                'page': 'Not Found',
            }
        return Response(data, status=status.HTTP_404_NOT_FOUND)


class FAQView(ListAPIView):
    def get(self, request, faq=None):
        if faq == 1:
            query = FAQ.objects.filter(status=1)
            ser = FAQSerializer(query, many=True)
            data = {
                'success': True,
                'queryset': ser.data
            }
        elif faq == 2:
            query = FAQ.objects.filter(status=2)
            ser = FAQSerializer(query, many=True)
            data = {
                'success': True,
                'queryset': ser.data
            }
        elif faq == 3:
            query = FAQ.objects.filter(status=3)
            ser = FAQSerializer(query, many=True)
            data = {
                'success': True,
                'queryset': ser.data
            }
        else:
            data = {
                'success': True,
                'page': 'Not Found'
            }
        return Response(data, status=status.HTTP_404_NOT_FOUND)


class TestimonialsView(ListAPIView):
    queryset = Testimonials.objects.all().order_by('-id')[:5]
    serializer_class = TestimonialsSerializer


class BlogView(ListAPIView):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer


class NewsView(ListAPIView):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer


class NewsFilterView(ListAPIView):
    def get(self, request, news=None):
        if news == 1:
            query = News.objects.filter(status=1)
            ser = NewsSerializer(query, many=True)
            data = {
                'success': True,
                'queryset': ser.data,
            }
        elif news == 2:
            query = News.objects.filter(status=2)
            ser = NewsSerializer(query, many=True)
            data = {
                'success': True,
                'queryset': ser.data,
            }
        else:
            data = {
                'success': True,
                'page': 'Not Found'
            }
        return Response(data, status=status.HTTP_404_NOT_FOUND)


class ConsultingView(CreateAPIView):
    queryset = Consulting.objects.all()
    serializer_class = ConsultingSerializer


class AppointmentView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class Aboutus_blogView(ListAPIView):
    queryset = Aboutus_blog.objects.all().order_by('-id')
    serializer_class = Aboutus_blogSerializer
