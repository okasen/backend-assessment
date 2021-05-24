# Our goal is to create a fullname field by concatenating a first and last name
import unittest
import task_1
import random


class TestFullNameCreated(unittest.TestCase):
    def setUp(self) -> None:
        self.user_records = task_1.create_full_name()
        self.record_to_test = random.choice(self.user_records)  #avoid wasting time testing every record
        self.split_name = self.record_to_test["full_name"].split()
        self.first_half = self.split_name[0]
        self.last_half = self.split_name[-1]

    def test_full_name_field_exists(self) -> None:
        self.assertTrue(self.record_to_test["full_name"])

    def test_full_name_is_string(self) -> None:
        self.assertEqual(type(self.record_to_test["full_name"]), str)

    def test_first_name_is_first(self) -> None:
        self.assertEqual(self.first_half, self.record_to_test["forename"])

    def test_last_name_is_last(self) -> None:
        self.assertEqual(self.last_half, self.record_to_test["surname"])

    def test_full_name_correct_format(self) -> None:  # names start with uppercase letter and are separated with a space
        self.assertRegex(self.record_to_test["full_name"], "^[A-Z].*[ ][A-Z].*$")
