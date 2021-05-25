# Our goal is to create a fullname field by concatenating a first and last name
import unittest
import task_1


class TestFullNameCreated(unittest.TestCase):
    def setUp(self) -> None:
        self.user_records = task_1.create_full_name()

    def test_full_name_field_exists(self) -> None:
        for record in self.user_records:
            self.assertTrue("full_name" in record)

    def test_full_name_is_string(self) -> None:
        for record in self.user_records:
            self.assertEqual(type(record["full_name"]), str)

    def test_full_name_correct_format(self) -> None:  # names start with uppercase letter and are separated with a space
        for record in self.user_records:
            self.assertRegex(record["full_name"], "^[A-Z].*[ ][A-Z].*$")
