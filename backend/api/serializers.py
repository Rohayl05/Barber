from rest_framework import serializers
from .models import Barber, Service, GalleryImage, ShopInfo
import json


class BarberSerializer(serializers.ModelSerializer):
    specialties_list = serializers.SerializerMethodField()

    class Meta:
        model = Barber
        fields = ['id', 'name', 'bio', 'image_url', 'specialties', 'specialties_list']

    def get_specialties_list(self, obj):
        if obj.specialties:
            return [s.strip() for s in obj.specialties.split(',')]
        return []


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'description', 'price', 'duration_minutes', 'category']


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'title', 'image_url', 'category', 'alt_text', 'uploaded_at']


class ShopInfoSerializer(serializers.ModelSerializer):
    opening_hours_parsed = serializers.SerializerMethodField()

    class Meta:
        model = ShopInfo
        fields = [
            'shop_name', 'tagline', 'phone', 'whatsapp', 'email', 'address',
            'google_maps_embed', 'fresha_url', 'fresha_shop_id',
            'opening_hours', 'opening_hours_parsed',
            'instagram', 'facebook',
            'hero_title', 'hero_subtitle', 'hero_image_url'
        ]

    def get_opening_hours_parsed(self, obj):
        try:
            return json.loads(obj.opening_hours)
        except (json.JSONDecodeError, TypeError):
            return {}
