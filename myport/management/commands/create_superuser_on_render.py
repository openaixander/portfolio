import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    """
    Custom management command to create a superuser if one does not exist.
    Reads credentials from environment variables.
    """
    help = 'Creates a superuser for the application from environment variables.'

    def handle(self, *args, **options):
        User = get_user_model()
        
        # Get credentials from environment variables
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if not email or not password:
            self.stdout.write(self.style.ERROR(
                'Missing DJANGO_SUPERUSER_EMAIL or DJANGO_SUPERUSER_PASSWORD environment variables.'
            ))
            return

        # Check if a user with this email already exists
        if not User.objects.filter(email=email).exists():
            self.stdout.write(self.style.SUCCESS(f'Creating superuser: {email}'))
            User.objects.create_superuser(email=email, password=password)
        else:
            self.stdout.write(self.style.WARNING(f'Superuser with email {email} already exists.'))