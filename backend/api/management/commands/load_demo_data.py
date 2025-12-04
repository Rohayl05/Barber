from django.core.management.base import BaseCommand
from api.models import Barber, Service, GalleryImage, ShopInfo


class Command(BaseCommand):
    help = 'Load demo data for StayFaded barbershop'

    def handle(self, *args, **options):
        self.stdout.write('Loading demo data...')
        
        # Clear existing data
        Barber.objects.all().delete()
        Service.objects.all().delete()
        GalleryImage.objects.all().delete()
        ShopInfo.objects.all().delete()
        
        # Create Shop Info
        shop = ShopInfo.objects.create(
            shop_name='STAY FADED',
            tagline='Stay Styled. Stay Confident. Stay Faded.',
            phone='',
            email='',
            address='392 St Saviours Rd, Leicester LE5 4HJ',
            opening_hours='{"monday": "9:00 AM - 6:00 PM", "tuesday": "9:00 AM - 6:00 PM", "wednesday": "9:00 AM - 6:00 PM", "thursday": "9:00 AM - 6:00 PM", "friday": "9:00 AM - 6:00 PM", "saturday": "9:00 AM - 6:00 PM", "sunday": "Closed"}',
            instagram='https://www.instagram.com/stayfadedbarbersuk/',
            facebook='',
            fresha_url='https://www.fresha.com/a/camthebarber-leicester-392-st-savious-rd-em8f1nii/booking?menu=true&pId=873537&dppub=true',
            hero_title='STAY STYLED. STAY CONFIDENT. STAY FADED.',
            hero_subtitle='At Stay Faded, we cater to your unique needs to elevate your style and confidence! Our skilled barbers provide top-notch haircuts and grooming with personalized styling advice.',
            hero_image_url='https://images.unsplash.com/photo-1585747860715-2ba37e788b70?q=80&w=2074&auto=format&fit=crop',
            google_maps_embed='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2421.5!2d-1.0936!3d52.6369!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4877612c1c5c1c1d%3A0x1234567890abcdef!2s392%20St%20Saviours%20Rd%2C%20Leicester%20LE5%204HJ!5e0!3m2!1sen!2suk!4v1701705600000'
        )
        self.stdout.write(self.style.SUCCESS(f'Created shop: {shop.shop_name}'))

        # Create Barbers (model has: name, bio, image_url, specialties, order, is_active)
        barbers_data = [
            {
                'name': 'Marcus Johnson',
                'bio': 'Master Barber & Founder | 15+ years experience\n\nMarcus has been cutting hair for over 15 years, training in London and New York. He founded StayFaded with a vision to create a space where classic barbering meets contemporary style. Known for his precision fades and attention to detail, Marcus has built a loyal clientele who trust him with their look.',
                'specialties': 'Skin Fades, Beard Sculpting, Hot Towel Shaves',
                'image_url': 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?q=80&w=400&auto=format&fit=crop',
                'is_active': True,
                'order': 1
            },
            {
                'name': 'Jayden Williams',
                'bio': 'Senior Barber | 8 years experience\n\nJayden specializes in modern cuts and creative designs. His background in art gives him a unique eye for shape and symmetry. Whether you want a clean professional look or something bold and expressive, Jayden delivers every time. He\'s particularly known for his intricate hair designs and lineup precision.',
                'specialties': 'Hair Designs, Lineups, Afro Styling',
                'image_url': 'https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=400&auto=format&fit=crop',
                'is_active': True,
                'order': 2
            },
            {
                'name': 'Daniel Thompson',
                'bio': 'Barber | 5 years experience\n\nDaniel brings energy and passion to every cut. Trained under Marcus, he\'s quickly become a client favorite for his friendly demeanor and consistent results. He excels at classic cuts and is the go-to for anyone wanting a timeless, clean look. Daniel believes every client should leave feeling confident.',
                'specialties': 'Classic Cuts, Scissor Work, Textured Crops',
                'image_url': 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?q=80&w=400&auto=format&fit=crop',
                'is_active': True,
                'order': 3
            },
            {
                'name': 'Chris Martinez',
                'bio': 'Junior Barber | 2 years experience\n\nChris is the newest member of the StayFaded team but don\'t let that fool you – his skills are sharp. A fast learner with natural talent, Chris is building his reputation one satisfied client at a time. He\'s eager to prove himself and offers excellent service at a great price point.',
                'specialties': 'Fades, Buzz Cuts, Student Cuts',
                'image_url': 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?q=80&w=400&auto=format&fit=crop',
                'is_active': True,
                'order': 4
            }
        ]

        for data in barbers_data:
            barber = Barber.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Created barber: {barber.name}'))

        # Create Services (model has: title, description, price, duration_minutes, category, order, is_active)
        # Based on actual Stay Faded services from Fresha
        services_data = [
            # Standard Services
            {
                'title': 'Hair and Beard - Extension',
                'description': 'Full haircut and beard grooming service with extended time for detailed work.',
                'price': 30.00,
                'duration_minutes': 60,
                'category': 'Standard Services',
                'is_active': True,
                'order': 1
            },
            {
                'title': 'Haircut',
                'description': 'Professional haircut tailored to your style. **Please note our 24-hour cancellation policy: If you cancel or reschedule your appointment within 24 hours, a fee may apply.',
                'price': 20.00,
                'duration_minutes': 30,
                'category': 'Standard Services',
                'is_active': True,
                'order': 2
            },
            {
                'title': 'Hair & Beard',
                'description': 'Haircut and beard trimming and shaping with blade. **Please note our 24-hour cancellation policy.',
                'price': 25.00,
                'duration_minutes': 30,
                'category': 'Standard Services',
                'is_active': True,
                'order': 3
            },
            # Beard Services
            {
                'title': 'Beard Trim',
                'description': 'Detailed beard line up and trim with a blade. **Please note our 24-hour cancellation policy.',
                'price': 10.00,
                'duration_minutes': 15,
                'category': 'Beard Services',
                'is_active': True,
                'order': 4
            },
            # Bundle Packages
            {
                'title': 'Haircut + Beard + Facial Treatment',
                'description': 'This package includes a haircut and beard and a facial treatment. **Please note our cancellation policy.',
                'price': 35.00,
                'duration_minutes': 60,
                'category': 'Bundle Packages',
                'is_active': True,
                'order': 5
            },
        ]

        for data in services_data:
            service = Service.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Created service: {service.title}'))

        # Create Gallery Images (model has: title, image_url, category, alt_text, order, is_active)
        gallery_data = [
            {
                'title': 'Clean Skin Fade',
                'image_url': 'https://images.unsplash.com/photo-1621605815971-fbc98d665033?q=80&w=800&auto=format&fit=crop',
                'category': 'fades',
                'alt_text': 'Precision skin fade with sharp lineup',
                'order': 1
            },
            {
                'title': 'Textured Crop',
                'image_url': 'https://images.unsplash.com/photo-1622286342621-4bd786c2447c?q=80&w=800&auto=format&fit=crop',
                'category': 'haircuts',
                'alt_text': 'Modern textured top with mid fade',
                'order': 2
            },
            {
                'title': 'Beard Sculpting',
                'image_url': 'https://images.unsplash.com/photo-1621607512214-68297480165e?q=80&w=800&auto=format&fit=crop',
                'category': 'beards',
                'alt_text': 'Full beard shape and detail work',
                'order': 3
            },
            {
                'title': 'Low Fade',
                'image_url': 'https://images.unsplash.com/photo-1599351431202-1e0f0137899a?q=80&w=800&auto=format&fit=crop',
                'category': 'fades',
                'alt_text': 'Subtle low fade with length on top',
                'order': 4
            },
            {
                'title': 'Classic Pompadour',
                'image_url': 'https://images.unsplash.com/photo-1503951914875-452162b0f3f1?q=80&w=800&auto=format&fit=crop',
                'category': 'haircuts',
                'alt_text': 'Timeless style with modern fade',
                'order': 5
            },
            {
                'title': 'Hair Design',
                'image_url': 'https://images.unsplash.com/photo-1634302086887-13b5281d6f75?q=80&w=800&auto=format&fit=crop',
                'category': 'styles',
                'alt_text': 'Custom geometric pattern',
                'order': 6
            },
            {
                'title': 'Shop Interior',
                'image_url': 'https://images.unsplash.com/photo-1585747860715-2ba37e788b70?q=80&w=800&auto=format&fit=crop',
                'category': 'shop',
                'alt_text': 'Our modern barbershop space',
                'order': 7
            },
            {
                'title': 'Mid Fade',
                'image_url': 'https://images.unsplash.com/photo-1596728325488-58c87691e9af?q=80&w=800&auto=format&fit=crop',
                'category': 'fades',
                'alt_text': 'Clean mid fade with waves',
                'order': 8
            },
            {
                'title': 'Straight Razor Shave',
                'image_url': 'https://images.unsplash.com/photo-1493256338651-d82f7acb2b38?q=80&w=800&auto=format&fit=crop',
                'category': 'beards',
                'alt_text': 'Traditional hot towel shave',
                'order': 9
            },
            {
                'title': 'Curly Top Fade',
                'image_url': 'https://images.unsplash.com/photo-1605497788044-5a32c7078486?q=80&w=800&auto=format&fit=crop',
                'category': 'haircuts',
                'alt_text': 'Natural curls with temple fade',
                'order': 10
            },
            {
                'title': 'Line Art Design',
                'image_url': 'https://images.unsplash.com/photo-1567894340315-735d7c361db0?q=80&w=800&auto=format&fit=crop',
                'category': 'styles',
                'alt_text': 'Intricate line work detail',
                'order': 11
            },
            {
                'title': 'Barber Station',
                'image_url': 'https://images.unsplash.com/photo-1503951914875-452162b0f3f1?q=80&w=800&auto=format&fit=crop',
                'category': 'shop',
                'alt_text': 'Professional setup',
                'order': 12
            },
        ]

        for data in gallery_data:
            image = GalleryImage.objects.create(**data)
            self.stdout.write(self.style.SUCCESS(f'Created gallery image: {image.title}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Demo data loaded successfully!'))
        self.stdout.write(f'   - 1 Shop Info')
        self.stdout.write(f'   - {Barber.objects.count()} Barbers')
        self.stdout.write(f'   - {Service.objects.count()} Services')
        self.stdout.write(f'   - {GalleryImage.objects.count()} Gallery Images')
