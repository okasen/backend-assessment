# Our goal is to create a fullname field by concatenating a first and last name
import unittest
from unittest.mock import patch
import task_1


class TestFullNameCreated(unittest.TestCase):

    def test_create_full_name(self) -> None:
        loaded_records = [{'forename': 'Steve', 'surname': 'Ortiz'}]

        result = task_1.FullNameCreator(loaded_records).create_full_name()

        self.assertEqual(result[0]["full_name"], "Steve Ortiz")

    def test_loaded_records_empty(self) -> None:
        loaded_records = []

        result = task_1.FullNameCreator(loaded_records).create_full_name()
        self.assertEqual(result, [])

    def test_create_full_name_multiple(self) -> None:
        loaded_records = [{'forename': 'Steve', 'surname': 'Ortiz'},{'forename': 'Jenni', 'surname': 'Black'}]

        result = task_1.FullNameCreator(loaded_records).create_full_name()
        self.assertEqual(len(result), 2)
