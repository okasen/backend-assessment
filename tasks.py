import json
from typing import Dict
import datetime
from dateutil.relativedelta import *


def load_records(filepath):
    with open(filepath) as user_records:
        loaded_records = json.load(user_records)

    return loaded_records


class FullNameFieldGenerator:
    def create_full_name(self) -> list[Dict]:
        for record in self.loaded_records:
            record["full_name"] = record["forename"] + " " + record["surname"]

        return self.loaded_records

    def __init__(self, loaded_records):
        self.loaded_records = loaded_records


class ThirtyPlusOnly:
    def __init__(self, loaded_records, todays_date):
        self.over_thirty_records = []
        self.loaded_records = loaded_records
        self.todays_date_full = todays_date
        self.age_to_test = 30

    def collect_over_thirty(self) -> list[Dict]:
        for record in self.loaded_records:
            date_of_birth = datetime.datetime.strptime(record["date_of_birth"], '%Y/%m/%d').date()
            age_in_years = relativedelta(self.todays_date_full, date_of_birth).years
            if age_in_years >= self.age_to_test:
                self.over_thirty_records.append(record)

        return self.over_thirty_records
