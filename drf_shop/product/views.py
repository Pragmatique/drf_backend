from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Product
from .serializers import ProductSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
