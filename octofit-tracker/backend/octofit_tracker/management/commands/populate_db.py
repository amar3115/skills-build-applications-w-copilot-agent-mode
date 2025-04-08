from django.core.management.base import BaseCommand
from octofit_tracker.models import YourModel  # Replace with your actual model

class Command(BaseCommand):
    help = 'Populate the database with test data for OctoFit Tracker'

    def handle(self, *args, **kwargs):
        # Example test data creation
        YourModel.objects.create(field1='Test Data 1', field2='Value 1')
        YourModel.objects.create(field1='Test Data 2', field2='Value 2')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
