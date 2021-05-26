import json
from typing import Dict
import datetime


def load_records(filepath):
    with open(filepath) as user_records:
        loaded_records = json.load(user_records)

    return loaded_records


class FullNameCreator():
    def create_full_name(self) -> Dict:
        for record in self.loaded_records:
            record["full_name"] = record["forename"] + " " + record["surname"]

        return self.loaded_records

    def __init__(self, loaded_records):
        self.loaded_records = loaded_records


class ThirtyPlusOnly():
    def __init__(self, loaded_records, todays_date):
        self.over_thirty_records = []
        self.loaded_records = loaded_records
        self.todays_date_full = todays_date
        self.today_year = int(self.todays_date_full.year)
        self.today_month = int(self.todays_date_full.month)
        self.today_day = int(self.todays_date_full.day)
        self.age_to_test = 30

    def collect_over_thirty(self) -> list:
        print(self.today_year)
        for record in self.loaded_records:
            split_dates = record["date_of_birth"].split("/")
            if int(split_dates[0]) < self.today_year - self.age_to_test:
                self.over_thirty_records.append(record)
            elif int(split_dates[0]) == self.today_year - self.age_to_test:
                if int(split_dates[1]) < self.today_month:
                    self.over_thirty_records.append(record)
                elif int(split_dates[1]) == self.today_month:
                    if int(split_dates[2]) <= self.today_day:
                        self.over_thirty_records.append(record)

        return self.over_thirty_records

