from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics

from .models import Category
from .serializers import CategorySerializer

class CategoriesApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

