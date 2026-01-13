import csv
from django.core.management.base import BaseCommand, CommandError
from ...models import Advertisement


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("csv_file_path", type=str)

    def handle(self, *args, **options):
        # CSV HEADER AD_URLS, DEPT_CODE, ZIP_CODE, CITY, CONDOMINIUM_EXPENSES

        if options["csv_file_path"].endswith(".csv") is False:
            raise CommandError("File must be .csv")

        with open(options["csv_file_path"], mode="r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                bienici_id = row["AD_URLS"].split("/")[-1]
                try:
                    condominium = float(row["CONDOMINIUM_EXPENSES"])
                except:
                    condominium = None
                Advertisement.objects.update_or_create(
                    bienici_id=bienici_id,
                    department=row["DEPT_CODE"],
                    city=row["CITY"],
                    zipcode=row["ZIP_CODE"],
                    condominium_fees=condominium,
                )

        self.stdout.write(self.style.SUCCESS("Successfully imported advertisements"))
