from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    help = 'Creates a superuser if none exists'

    def handle(self, *args, **kwargs):

        if not User.objects.filter(is_superuser=True).exists():
            self.stdout.write(self.style.SUCCESS('Superuser not found. Creating a new one...'))
            
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='password'
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))

        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists.'))