import json
from typing import Dict, List
import datetime
from dateutil.relativedelta import relativedelta


def load_records(filepath):
    with open(filepath) as user_records:
        loaded_records = json.load(user_records)

    return loaded_records


def load_company_records(filepath):
    with open(filepath) as company_records:
        loaded_company_records = json.load(company_records)

    return loaded_company_records


class FullNameFieldGenerator:
    def create_full_name(self) -> List[Dict]:
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

    def collect_over_thirty(self) -> List[Dict]:
        for record in self.loaded_records:
            date_of_birth = datetime.datetime.strptime(record["date_of_birth"], '%Y/%m/%d').date()
            age_in_years = relativedelta(self.todays_date_full, date_of_birth).years
            if age_in_years >= self.age_to_test:
                self.over_thirty_records.append(record)

        return self.over_thirty_records


class CompanyFieldGenerator:
    def __init__(self, user_records, company_records) -> None:
        self.user_records = user_records
        self.company_records = company_records

    def company_id_to_field(self) -> List[Dict]:
        for record in self.user_records:
            if "company_id" in record:
                matching_company = list(filter(lambda match: match["id"] == record["company_id"], self.company_records))
                if len(matching_company) > 0:
                    record["company"] = matching_company[0] # in case there are multiple matches, we'll pick the first
                    del record["company_id"]  # only popping if there's a company record to replace the id!

        # if any of these if-statements fail, I just want to return the input record that was given with no changes
        return self.user_records
