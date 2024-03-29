"""Tests for faker-nonprofit provider."""

import unittest
from faker import Faker, Generator

import faker_nonprofit


class IntegrationTestCase(unittest.TestCase):
    """Integration tests."""

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(faker_nonprofit.Provider)

    def test_integration(self):
        """Test integration with Faker."""
        result = self.fake.nonprofit_name()
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 1)


class NonProfitProviderTestCase(unittest.TestCase):
    """Provider test case."""

    def setUp(self):
        self.fake = Faker()
        self.fake.add_provider(faker_nonprofit.Provider)

    def test_lists_in_order(self):
        """Test internal values are in order."""
        for attr_name, attr in faker_nonprofit.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assert_list_in_order(attr)

    def assert_list_in_order(self, the_list):
        """Assert a list is in order."""
        prev_value = ""
        for this_value in the_list:
            self.assertGreaterEqual(this_value, prev_value)
            prev_value = this_value

    def test_no_duplicates(self):
        """Test value lists don't contain duplicates."""
        for attr_name, attr in faker_nonprofit.__dict__.items():
            with self.subTest(attr_name=attr_name):
                if isinstance(attr, list):
                    self.assertEqual(len(attr), len(set(attr)))

    def test_words(self):
        """Test that generated string is at least two words long."""
        name = self.fake.nonprofit_name()
        word_count = len(name.split())
        self.assertGreaterEqual(word_count, 2)

    def test_job_titles(self):
        """Test that the generated titles returns a valid value."""
        title = self.fake.nonprofit_title()
        self.assertIn(title, faker_nonprofit.JOB_TITLES,
                      'Provided title not from list')

    def test_foundation_name(self):
        """Test that the generated foundation names returns a valid value."""
        # Due to use of random selection within the method, using multiple calls.
        for x in range(10):
            fund = self.fake.foundation_name()
        word_count = len(fund.split())
        self.assertGreaterEqual(word_count, 2)

if __name__ == "__main__":
    unittest.main()
