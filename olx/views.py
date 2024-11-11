from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework import filters, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response

def HomeView(requests):
    categories = Category.objects.all()
    return render(requests, 'index2.html')

class JobsViewset(ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = ListJobs
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['location']
    filterset_fields = ['posted_on', 'job_type']
    ordering_fields = '__all__'

class ImageViewSet(ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer

class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['name', 'code']
    ordering_fields = '__all__'

class SizeViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class VariantsViewSet(ModelViewSet):
    queryset = Variants.objects.all()
    serializer_class = VariantsSerializer

class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'keyword']
    filterset_fields = ['title', 'id', 'keyword']
    ordering_fields = '__all__'