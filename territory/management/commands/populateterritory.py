import os
from django.core.management.base import BaseCommand
from territory.models import TerritorialUnit, Location
from ._privateterritory import import_territorial_unit_data, import_location_data


class Command(BaseCommand):
    help = 'Add territorial units'

    def handle(self, *args, **options):

        territorial_units_file_path = os.path.join(os.path.dirname(
            __file__), '..', '..', 'datafiles', 'TERC_Urzedowy_2024-03-21.csv')
        import_territorial_unit_data(territorial_units_file_path)
        territorial_unit_count = TerritorialUnit.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f"Territorial units added. Total: {territorial_unit_count}."))

        location_file_path = os.path.join(os.path.dirname(
            __file__), '..', '..', 'datafiles', 'SIMC_Urzedowy_2024-03-21.csv')
        import_location_data(location_file_path)
        location_count = Location.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f"Locations added. Total: {location_count}."))
