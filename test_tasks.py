# Our goal is to create a fullname field by concatenating a first and last name
import unittest
import tasks
import datetime


class TestFullNameCreated(unittest.TestCase):

    def test_create_full_name(self) -> None:
        loaded_records = [{'forename': 'Steve', 'surname': 'Ortiz'}]

        result = tasks.FullNameFieldGenerator(loaded_records).create_full_name()

        self.assertEqual(result[0]["full_name"], "Steve Ortiz")

    def test_loaded_records_empty(self) -> None:
        loaded_records = []

        result = tasks.FullNameFieldGenerator(loaded_records).create_full_name()
        self.assertEqual(result, [])

    def test_create_full_name_multiple(self) -> None:
        loaded_records = [{'forename': 'Steve', 'surname': 'Ortiz'}, {'forename': 'Jenni', 'surname': 'Black'}]

        result = tasks.FullNameFieldGenerator(loaded_records).create_full_name()
        self.assertEqual(len(result), 2)


class TestOverThirty(unittest.TestCase):

    def setUp(self) -> None:
        self.test_date = datetime.date(2021, 5, 26)

    def test_is_under_thirty(self) -> None:
        loaded_records = [{'full_name': "Jennifer Black", 'date_of_birth': "1995/05/04"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [])

    def test_over_thirty_year(self) -> None:
        loaded_records = [{'full_name': "Jen Eric", "date_of_birth": "1990/05/04"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [{'full_name': "Jen Eric", "date_of_birth": "1990/05/04"}])

    def test_over_and_under(self) -> None:
        loaded_records = [{'full_name': "Jen Eric", "date_of_birth": "1990/05/04"},
                          {'full_name': "Jennifer Black", 'date_of_birth': "1995/05/04"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [{'full_name': "Jen Eric", "date_of_birth": "1990/05/04"}])

    def test_over_by_month_not_year(self) -> None:
        loaded_records = [{'full_name': "Mick Chicken", "date_of_birth": "1991/04/04"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [{'full_name': "Mick Chicken", "date_of_birth": "1991/04/04"}])

    def test_under_by_month(self) -> None:
        loaded_records = [{'full_name': "Chicken Little", "date_of_birth": "1991/06/04"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [])

    def test_under_and_over_month(self) -> None:
        loaded_records = [{'full_name': "Chicken Little", "date_of_birth": "1991/06/04"},
                          {'full_name': "Mick Chicken", "date_of_birth": "1991/04/04"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [{'full_name': "Mick Chicken", "date_of_birth": "1991/04/04"}])

    def test_under_and_over_day(self) -> None:
        loaded_records = [{'full_name': "Thing One", "date_of_birth": "1991/05/25"},
                          {'full_name': "Thing Two", "date_of_birth": "1991/05/27"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [{'full_name': "Thing One", "date_of_birth": "1991/05/25"}])

    def test_exact_day(self) -> None:
        loaded_records = [{'full_name': "Birthday Boy", "date_of_birth": "1991/05/26"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [{'full_name': "Birthday Boy", "date_of_birth": "1991/05/26"}])

    def test_multiple_dates(self) -> None:
        loaded_records = [{'full_name': "Jennifer Black", 'date_of_birth': "1995/05/04"},
                          {'full_name': "Jen Eric", "date_of_birth": "1990/05/04"},
                          {'full_name': "Chicken Little", "date_of_birth": "1991/06/04"},
                          {'full_name': "Mick Chicken", "date_of_birth": "1991/04/04"},
                          {'full_name': "Thing One", "date_of_birth": "1991/05/25"},
                          {'full_name': "Thing Two", "date_of_birth": "1991/05/27"}]

        result = tasks.ThirtyPlusOnly(loaded_records, self.test_date).collect_over_thirty()
        self.assertEqual(result, [{'full_name': "Jen Eric", "date_of_birth": "1990/05/04"},
                                  {'full_name': "Mick Chicken", "date_of_birth": "1991/04/04"},
                                  {'full_name': "Thing One", "date_of_birth": "1991/05/25"}])
