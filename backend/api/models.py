from django.db import models


class Barber(models.Model):
    """Barber profile model."""
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    specialties = models.CharField(max_length=200, blank=True, help_text="Comma-separated specialties")
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Service(models.Model):
    """Service offered by the barber shop."""
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration_minutes = models.PositiveIntegerField(help_text="Duration in minutes")
    category = models.CharField(max_length=50, blank=True, help_text="e.g., Haircuts, Beard, Combo")
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['category', 'order', 'title']

    def __str__(self):
        return f"{self.title} - ${self.price}"


class GalleryImage(models.Model):
    """Gallery image for showcasing work."""
    CATEGORY_CHOICES = [
        ('haircuts', 'Haircuts'),
        ('beards', 'Beards'),
        ('fades', 'Fades'),
        ('styles', 'Styles'),
        ('shop', 'Shop'),
    ]
    
    title = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(max_length=500)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='haircuts')
    alt_text = models.CharField(max_length=200, blank=True, help_text="Image alt text for accessibility")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'order', '-uploaded_at']
        verbose_name = 'Gallery Image'
        verbose_name_plural = 'Gallery Images'

    def __str__(self):
        return self.title or f"Image {self.pk}"


class ShopInfo(models.Model):
    """Shop contact information and settings (singleton)."""
    shop_name = models.CharField(max_length=100, default="Barber Shop")
    tagline = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    whatsapp = models.CharField(max_length=20, blank=True, help_text="WhatsApp number with country code")
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    google_maps_embed = models.TextField(blank=True, help_text="Google Maps iframe embed code")
    fresha_url = models.URLField(blank=True, help_text="Fresha booking URL")
    fresha_shop_id = models.CharField(max_length=50, blank=True, help_text="Fresha shop ID for widget")
    
    # Opening hours stored as JSON-like text
    opening_hours = models.TextField(
        blank=True,
        default='{"monday": "9:00 - 19:00", "tuesday": "9:00 - 19:00", "wednesday": "9:00 - 19:00", "thursday": "9:00 - 19:00", "friday": "9:00 - 19:00", "saturday": "9:00 - 17:00", "sunday": "Closed"}',
        help_text="JSON format opening hours"
    )
    
    # Social media
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    
    # Hero section
    hero_title = models.CharField(max_length=200, default="Premium Grooming Experience")
    hero_subtitle = models.TextField(blank=True, default="Expert cuts, classic shaves, and modern styles.")
    hero_image_url = models.URLField(max_length=500, blank=True)
    
    class Meta:
        verbose_name = 'Shop Information'
        verbose_name_plural = 'Shop Information'

    def __str__(self):
        return self.shop_name

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
