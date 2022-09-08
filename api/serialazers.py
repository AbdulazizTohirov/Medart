from rest_framework import serializers
from main.models import *

# Info M0del Serializer
class Infoserializer(serializers.ModelSerializer):
    class Meta:
        model = InfoModel
        fields ='__all__'

# Our Services Serializer
class OurServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurServicesModel
        fields = '__all__'
    
# Link Serializer
class LinkSerializer(serializers.ModelSerializer):
      class Meta:
        model = LinkModel
        fields = '__all__'
    
# Contact Serializer
class ContactSerializer(serializers.ModelSerializer):
      class Meta:
        model = ContactModel
        fields = '__all__'

# About Us Block  Serializer
class AboutusNlockSerializer(serializers.ModelSerializer):
      class Meta:
        model = AboutusblockModel
        fields = '__all__'

# Doctors Serializer
class DoctorsSerializer(serializers.ModelSerializer):
      class Meta:
        model = Doctors
        fields = '__all__'

# Operationg Attented  Serializer
class Operetion_Attented_Serializer(serializers.ModelSerializer):
      class Meta:
        model = Operationg_Attented
        fields = '__all__'

# Doctors Detail Serializer
class DoctorsDetailSerializer(serializers.ModelSerializer):
      class Meta:
        model = Doctors_detail
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











































