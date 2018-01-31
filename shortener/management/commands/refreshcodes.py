from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShortenUrl

class Command(BaseCommand):
    help = 'Refreshes all Url shortcodes.'
    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)
    def handle(self, *args, **options):
        print(options)
        return ShortenUrl.objects.refresh_shortcode(items=options['items'])
        