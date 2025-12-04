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
            shop_name='STAYFADED',
            tagline='Premium cuts. Fresh fades. Modern style.',
            phone='+44 20 7123 4567',
            email='bookings@stayfaded.co.uk',
            address='127 High Street, Shoreditch, London E1 6JN',
            opening_hours='{"monday": "9:00 AM - 7:00 PM", "tuesday": "9:00 AM - 7:00 PM", "wednesday": "9:00 AM - 7:00 PM", "thursday": "9:00 AM - 8:00 PM", "friday": "9:00 AM - 8:00 PM", "saturday": "8:00 AM - 6:00 PM", "sunday": "Closed"}',
            instagram='https://instagram.com/stayfaded',
            facebook='https://facebook.com/stayfaded',
            fresha_url='https://www.fresha.com',
            hero_title='STAY FRESH. STAY FADED.',
            hero_subtitle='Premium cuts, fresh fades, and modern styles in the heart of London.',
            hero_image_url='https://images.unsplash.com/photo-1585747860715-2ba37e788b70?q=80&w=2074&auto=format&fit=crop',
            google_maps_embed='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2482.4!2d-0.0777!3d51.5234!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zNTHCsDMxJzI0LjIiTiAwwrAwNCczOS43Ilc!5e0!3m2!1sen!2suk!4v1234567890'
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
        services_data = [
            # Haircuts
            {
                'title': 'Signature Fade',
                'description': 'Our signature skin fade with precision lineup. Includes consultation, wash, cut, and style.',
                'price': 35.00,
                'duration_minutes': 45,
                'category': 'Haircuts',
                'is_active': True,
                'order': 1
            },
            {
                'title': 'Classic Cut',
                'description': 'Traditional scissor cut for a timeless look. Perfect for professional settings.',
                'price': 28.00,
                'duration_minutes': 30,
                'category': 'Haircuts',
                'is_active': True,
                'order': 2
            },
            {
                'title': 'Buzz Cut',
                'description': 'Clean and simple all-over clipper cut. Low maintenance, high impact.',
                'price': 18.00,
                'duration_minutes': 20,
                'category': 'Haircuts',
                'is_active': True,
                'order': 3
            },
            {
                'title': 'Skin Fade',
                'description': 'Seamless fade from skin to your desired length on top. Sharp and modern.',
                'price': 32.00,
                'duration_minutes': 40,
                'category': 'Haircuts',
                'is_active': True,
                'order': 4
            },
            {
                'title': 'Textured Crop',
                'description': 'Modern textured top with faded sides. The trendy cut everyone\'s asking for.',
                'price': 30.00,
                'duration_minutes': 35,
                'category': 'Haircuts',
                'is_active': True,
                'order': 5
            },
            {
                'title': 'Kids Cut (Under 12)',
                'description': 'Full haircut service for the little ones. Patient and friendly service guaranteed.',
                'price': 18.00,
                'duration_minutes': 25,
                'category': 'Haircuts',
                'is_active': True,
                'order': 6
            },
            # Beard
            {
                'title': 'Beard Trim',
                'description': 'Shape and trim your beard to perfection. Includes line-up and oil finish.',
                'price': 15.00,
                'duration_minutes': 20,
                'category': 'Beard',
                'is_active': True,
                'order': 7
            },
            {
                'title': 'Beard Sculpt',
                'description': 'Full beard shaping and design. Transform your facial hair into a work of art.',
                'price': 22.00,
                'duration_minutes': 30,
                'category': 'Beard',
                'is_active': True,
                'order': 8
            },
            {
                'title': 'Hot Towel Shave',
                'description': 'Traditional straight razor shave with hot towels and premium products. The ultimate luxury.',
                'price': 30.00,
                'duration_minutes': 35,
                'category': 'Beard',
                'is_active': True,
                'order': 9
            },
            # Packages
            {
                'title': 'The Full Works',
                'description': 'Haircut + Beard Trim + Hot Towel Face Treatment. Complete grooming experience.',
                'price': 55.00,
                'duration_minutes': 75,
                'category': 'Combo',
                'is_active': True,
                'order': 10
            },
            {
                'title': 'Cut & Beard Combo',
                'description': 'Any haircut with a beard trim. Save £5 on the combo.',
                'price': 42.00,
                'duration_minutes': 55,
                'category': 'Combo',
                'is_active': True,
                'order': 11
            },
            {
                'title': 'Father & Son',
                'description': 'One adult cut and one kids cut. Quality time, fresh cuts.',
                'price': 45.00,
                'duration_minutes': 60,
                'category': 'Combo',
                'is_active': True,
                'order': 12
            },
            # Extras
            {
                'title': 'Hair Design',
                'description': 'Custom designs and patterns carved into your fade. Express yourself.',
                'price': 10.00,
                'duration_minutes': 15,
                'category': 'Extras',
                'is_active': True,
                'order': 13
            },
            {
                'title': 'Eyebrow Tidy',
                'description': 'Clean up and shape your eyebrows for a polished look.',
                'price': 8.00,
                'duration_minutes': 10,
                'category': 'Extras',
                'is_active': True,
                'order': 14
            },
            {
                'title': 'Grey Blending',
                'description': 'Subtle colour treatment to blend away grey hairs naturally.',
                'price': 20.00,
                'duration_minutes': 25,
                'category': 'Extras',
                'is_active': True,
                'order': 15
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
