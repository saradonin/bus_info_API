import csv
from datetime import datetime
from territory.models import TerritorialUnit, Location


def import_territorial_unit_data(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data_dict = {
                'name': row['NAZWA'],
                'type_name': row['NAZWA_DOD'],
                'region': row.get('WOJ'),
                'county': row.get('POW'),
                'community': row.get('GMI'),
                'type': row.get('RODZ'),
                'date': datetime.strptime(row['STAN_NA'], '%Y-%m-%d').date()
            }
            if not TerritorialUnit.objects.filter(**data_dict).exists():
                TerritorialUnit.objects.create(**data_dict)


def import_location_data(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            data_dict = {
                'name': row['NAZWA'],
                'region': row['WOJ'],
                'county': row['POW'],
                'community': row['GMI'],
                'community_type': row['RODZ_GMI'],
                'location_type': row['RM'],
                'symbol': row['SYM'],
                'parent_symbol': row['SYMPOD'],
                'date': datetime.strptime(row['STAN_NA'], '%Y-%m-%d').date()
            }
            if Location.objects.filter(symbol=data_dict['symbol']).exists():
                existing_location = Location.objects.get(
                    symbol=data_dict['symbol'])

                if any(getattr(existing_location, field) != value for field, value in data_dict.items()):
                    for key, value in data_dict.items():
                        setattr(existing_location, key, value)
                    existing_location.save()
            else:
                Location.objects.create(**data_dict)
