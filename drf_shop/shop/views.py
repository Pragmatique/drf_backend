from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Shop, ShopItem, ShopClient
from .serializers import ShopSerializer, ShopItemSerializer, ShopClientSerializer
from .permissions import IsAdmin

# Create your views here.
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]


class ShopItemViewSet(viewsets.ModelViewSet):
    queryset = ShopItem.objects.all()
    serializer_class = ShopItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]


class ShopClientViewSet(viewsets.ModelViewSet):
    queryset = ShopClient.objects.all()
    serializer_class = ShopClientSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]