from .models import *
from rest_framework.generics import ListAPIView
from api.serializers import *



class NewsView(ListAPIView):
    queryset = News.objects.all().order_by('-id')
    serializer_class = NewsSerializer

