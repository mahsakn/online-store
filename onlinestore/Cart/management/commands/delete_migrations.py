import os

from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = ('Delete all migration files from all apps')

    def handle(self, *args, **kwargs):
        char = '-'
        apps = [app for app in settings.INSTALLED_APPS if not app.startswith("django") and not char in app]
        # apps.remove('pages')
        print(apps)
        for app in apps:
            os.system(f'python manage.py migrate {app} zero ')
            print("\033[95m", f"!!!  {app}  MIGRATES HAS BEEN UNAPPLIED !!!")
        for app in apps:
            os.system(f'find . -path "*/{app}/migrations/*.py" -not -name "__init__.py" -delete')
            print(f"!!!  {app}  MIGRATIONS HAS BEEN DELETED !!!")
