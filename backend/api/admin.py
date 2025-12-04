from django.contrib import admin
from .models import Barber, Service, GalleryImage, ShopInfo


@admin.register(Barber)
class BarberAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialties', 'order', 'is_active', 'created_at']
    list_filter = ['is_active']
    search_fields = ['name', 'bio']
    ordering = ['order', 'name']
    list_editable = ['order', 'is_active']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'duration_minutes', 'category', 'order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'description']
    ordering = ['category', 'order', 'title']
    list_editable = ['price', 'order', 'is_active']


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'order', 'is_active', 'uploaded_at']
    list_filter = ['category', 'is_active']
    search_fields = ['title', 'alt_text']
    ordering = ['category', 'order', '-uploaded_at']
    list_editable = ['category', 'order', 'is_active']


@admin.register(ShopInfo)
class ShopInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Info', {
            'fields': ('shop_name', 'tagline', 'phone', 'whatsapp', 'email')
        }),
        ('Location', {
            'fields': ('address', 'google_maps_embed')
        }),
        ('Booking', {
            'fields': ('fresha_url', 'fresha_shop_id')
        }),
        ('Hours', {
            'fields': ('opening_hours',)
        }),
        ('Social Media', {
            'fields': ('instagram', 'facebook')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_image_url')
        }),
    )

    def has_add_permission(self, request):
        # Prevent adding more than one instance
        return not ShopInfo.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
