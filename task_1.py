import json
from typing import Dict


def create_full_name() -> Dict:
    with open('./assets/user.json') as user_records:
        loaded_records = json.load(user_records)

    for record in loaded_records:
        record["full_name"] = record["forename"] + " " + record["surname"]

    return loaded_records
