import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from dotenv import load_dotenv

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a superuser from environment variables'

    def handle(self, *args, **options):
        load_dotenv()
        email = os.environ.get('SUPERUSER_EMAIL')
        password = os.environ.get('SUPERUSER_PASSWORD')
        
        if not email or not password:
            self.stdout.write(self.style.ERROR('Superuser email or password not set in environment variables'))
            return
            
        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING(f'Superuser with email {email} already exists'))
            return
            
        User.objects.create_superuser(email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Superuser {email} created successfully'))