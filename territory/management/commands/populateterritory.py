import os
from django.core.management.base import BaseCommand
from territory.models import TerritorialUnit
from ._privateterritory import import_territorial_unit_data


class Command(BaseCommand):
    help = 'Add territorial units'

    def handle(self, *args, **options):
        if not TerritorialUnit.objects.exists():
            csv_file_path = os.path.join(os.path.dirname(
                __file__), '..', '..', 'datafiles', 'TERC_Urzedowy_2024-03-21.csv')
            import_territorial_unit_data(csv_file_path)
            self.stdout.write(self.style.SUCCESS("Terrotorial units added"))
