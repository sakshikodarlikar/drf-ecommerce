from django.db.models import fields
from rest_framework import serializers
from .models import *

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('id', 'created_at', 'updated_at')

# Buyer Serializer
class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        exclude = ('id', 'buyer_created_date', 'buyer_updated_date')

#Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ('id', 'order_created_date', 'order_updated_date')

#Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        exclude = ('id',)

#Seller Serializer
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('id', 'seller_created_date', 'seller_updated_date')
    
