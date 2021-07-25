from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('product',views.ProductViewSet, basename='ProductViewSet')
router.register('category',views.CategoryViewSet, basename='CategoryViewSet')
router.register('buyer',views.BuyerViewSet, basename='BuyerViewSet')
router.register('seller',views.SellerViewSet, basename='SellerViewSet')
router.register('order',views.OrderViewSet, basename='OrderViewSet')

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', include(router.urls), name='viewset'),    

]
