from rest_framework import serializers
from .models import Shop, ShopItem, ShopClient


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id','name','owner')


class ShopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItem
        fields = ('id','shop','product')


class ShopClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopClient
        fields = ('id','shop','client')