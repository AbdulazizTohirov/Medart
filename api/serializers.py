from rest_framework import serializers
from main.models import *

# Info M0del Serializer
class Infoserializer(serializers.ModelSerializer):
    class Meta:
        model = InfoModel
        fields ='__all__'

    
# Doctors Serializer
class DoctorsSerializer(serializers.ModelSerializer):
      class Meta:
        model = Doctors
        fields = '__all__'

# Operationg Attented  Serializer
class Operetion_Attented_Serializer(serializers.ModelSerializer):
      class Meta:
        depth = 1
        model = Operationg_Attented
        fields = '__all__'

# Doctors Detail Serializer
class DoctorsAboutSerializer(serializers.ModelSerializer):
      class Meta:
        depth = 1
        model = Doctors_about
        fields = '__all__'

# FAQ Serializer
class FAQSerializer(serializers.ModelSerializer):
      class Meta:
        model = FAQ
        fields = '__all__'

# Testimonials Serializer
class TestimonialsSerializer(serializers.ModelSerializer):
      class Meta:
        model = Testimonials
        fields = '__all__'

# Blog Serializer
class BlogSerializer(serializers.ModelSerializer):
      class Meta:
        model = Blog
        fields = '__all__'

# News Serializer
class NewsSerializer(serializers.ModelSerializer):
      class Meta:
        model = News
        fields = '__all__'
    
# OurService Serializer
class OurServiceSerializer(serializers.ModelSerializer):
      class Meta:
        model = OurService
        fields = '__all__'

# Introduction Serializer
class IntroductionSerializer(serializers.ModelSerializer):
      class Meta:
        model = Introduction
        fields = '__all__'

# Consulting Serializer
class ConsultingSerializer(serializers.ModelSerializer):
      class Meta:
        model = Consulting
        fields = '__all__'

# Appointment Serializer
class AppointmentSerializer(serializers.ModelSerializer):
      class Meta:
        model = Appointment
        fields = '__all__'

# Aboutus_blog Serializer
class Aboutus_blogSerializer(serializers.ModelSerializer):
      class Meta:
        model = Aboutus_block
        fields = '__all__'











































