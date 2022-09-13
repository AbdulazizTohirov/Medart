from main.models import *
from rest_framework import serializers


class Infoserializer(serializers.ModelSerializer):
    class Meta:
        model = InfoModel
        fields ='__all__'


class DoctorsSerializer(serializers.ModelSerializer):
      class Meta:
        model = Doctors
        fields = '__all__'


class Operetion_Attented_Serializer(serializers.ModelSerializer):
      class Meta:
        depth = 1
        model = Operationg_Attented
        fields = '__all__'


class DoctorsAboutSerializer(serializers.ModelSerializer):
      class Meta:
        depth = 2
        model = Doctors_about
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
      class Meta:
        model = FAQ
        fields = '__all__'


class TestimonialsSerializer(serializers.ModelSerializer):
      class Meta:
        model = Testimonials
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
      class Meta:
        model = Blog
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
      class Meta:
        model = News
        fields = '__all__'


class OurServiceSerializer(serializers.ModelSerializer):
      class Meta:
        model = OurService
        fields = '__all__'


# class IntroductionSerializer(serializers.ModelSerializer):
#       class Meta:
#         model = Introduction
#         fields = '__all__'


class ConsultingSerializer(serializers.ModelSerializer):
      class Meta:
        model = Consulting
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
      class Meta:
        model = Appointment
        fields = '__all__'


class Aboutus_blogSerializer(serializers.ModelSerializer):
      class Meta:
        model = Aboutus_blog
        fields = '__all__'