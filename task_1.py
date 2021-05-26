import json
from typing import Dict


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