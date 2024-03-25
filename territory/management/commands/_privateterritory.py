import csv
from datetime import datetime
from territory.models import TerritorialUnit


def import_territorial_unit_data(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            print(row)
            region = row['WOJ']
            county = row.get('POW')
            community = row.get('GMI')
            type = row.get('RODZ')
            name = row['NAZWA']
            type_name = row['NAZWA_DOD']
            date_str = row['STAN_NA']
            date = datetime.strptime(date_str, '%Y-%m-%d').date()

            territorial_unit = TerritorialUnit(
                name=name,
                type_name=type_name,
                region=region,
                county=county,
                community=community,
                type=type,
                date=date
            )
            territorial_unit.save()


