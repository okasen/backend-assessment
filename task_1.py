import json
from typing import Dict

class FullNameCreator():
    def load_records(self):
        with open('./assets/user.json') as user_records:
            self.loaded_records = json.load(user_records)

    def create_full_name(self) -> Dict:
        for record in self.loaded_records:
            record["full_name"] = record["forename"] + " " + record["surname"]

        return self.loaded_records
