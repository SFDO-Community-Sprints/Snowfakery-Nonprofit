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
        self.provider = faker_nonprofit.Provider(Generator())

    def test_lists_in_order(self):
        """Test interal values are in order."""
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
        name = self.provider.nonprofit_name()
        word_count = len(name.split())
        self.assertGreaterEqual(word_count, 2)


if __name__ == "__main__":
    unittest.main()
