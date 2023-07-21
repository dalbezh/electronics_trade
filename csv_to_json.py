import os
import csv
import json
import re
from pathlib import Path

CSV_PATH = Path(__file__).parent.joinpath("datasets")
JSON_PATH = Path(__file__).parent.joinpath("fixtures")
CSV_FILES = list(map(lambda x: f"{CSV_PATH}/{x}", os.listdir(path=CSV_PATH)))


def csv_to_json(csv_file: str, json_file: str):
    """
    Работает через консоль:
    python csv_to_json.py
    """
    main_list = []

    with open(csv_file, encoding='utf-8-sig') as data:
        csv_reader = csv.DictReader(data, delimiter=";")
        for row in csv_reader:
            row["id"] = int(row["id"])

            if csv_file.endswith('/organization.csv'):
                model = "orgs.organization"
                row["organization_form"] = int(row["organization_form"])

            if csv_file.endswith('/organization_products.csv'):
                model = "orgs.organization_products"
                row["organization_id"] = int(row["organization_id"])
                row["product_id"] = int(row["product_id"])

            if csv_file.endswith('/products.csv'):
                model = "orgs.product"

            if csv_file.endswith('/providerorganization.csv'):
                model = "orgs.providerorganization"
                row["debt"] = float(row["debt"])
                row["provider_id"] = int(row["provider_id"])
                row["seller_id"] = int(row["seller_id"])

            main_list.append({"model": model, "fields": row})

    with open(json_file, 'w', encoding='utf-8') as data:
        json_data = json.dumps(main_list, indent=4, ensure_ascii=False)
        data.write(json_data)


if __name__ == "__main__":
    for csv_file in CSV_FILES:
        if os.path.isfile(csv_file):
            json_file = f"{JSON_PATH}/{re.split('[/.]', csv_file)[-2]}.json"
            csv_to_json(csv_file, json_file)
