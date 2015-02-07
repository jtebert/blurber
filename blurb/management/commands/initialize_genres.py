from django.core.management import BaseCommand

class Command(BaseCommand):
    def handle(*args, **kwargs):
        print("I am running!")