from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication






# Create your views here.
def index(request):
    # return render(request, 'mainapp/index.html')
    pass

# Product Generic Viewset 
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
        
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Category Generic View
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


# Buyer Generic Viewset
class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer

# Seller Generic Viewset
class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

# Oders Generic Viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer




