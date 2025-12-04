from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Barber, Service, GalleryImage, ShopInfo
from .serializers import (
    BarberSerializer, 
    ServiceSerializer, 
    GalleryImageSerializer, 
    ShopInfoSerializer
)


class BarberViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for barber profiles."""
    queryset = Barber.objects.filter(is_active=True)
    serializer_class = BarberSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for services."""
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)
        return queryset


class GalleryImageViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint for gallery images."""
    queryset = GalleryImage.objects.filter(is_active=True)
    serializer_class = GalleryImageSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)
        return queryset


class ShopInfoView(views.APIView):
    """API endpoint for shop information (singleton)."""
    
    def get(self, request):
        shop_info = ShopInfo.get_instance()
        serializer = ShopInfoSerializer(shop_info)
        return Response(serializer.data)


@api_view(['GET'])
def health_check(request):
    """Health check endpoint for deployment."""
    return Response({'status': 'healthy', 'message': 'Barber Shop API is running'})
