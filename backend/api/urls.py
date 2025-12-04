from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'barbers', views.BarberViewSet, basename='barber')
router.register(r'services', views.ServiceViewSet, basename='service')
router.register(r'gallery', views.GalleryImageViewSet, basename='gallery')

urlpatterns = [
    path('', include(router.urls)),
    path('shop-info/', views.ShopInfoView.as_view(), name='shop-info'),
    path('health/', views.health_check, name='health-check'),
]
