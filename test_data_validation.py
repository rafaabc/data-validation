import unittest
import pandas as pd
from parameterized import parameterized


class TestDataValidationV3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load the dataset once before all test cases
        cls.data = pd.read_csv("dataset.csv")

    """Checks that the data in each field, column, list, range or file corresponds to the correct type and
        format e.g.: int, str, bool, etc."""
    @parameterized.expand([
        ("Name", str),
        ("Age", int),
        ("Email", str),
        ("Subscriber", str)
    ])
    def test_data_type_validation(self, column, expected_type):
        with self.subTest(column=column):
            # Check data types
            self.assertTrue((self.data[column].apply(type) == expected_type).all(),
                            f"{column} should be of type {expected_type.__name__}")

    """Checks that the data meets valid value ranges or expectations e.g.: age field has a valid age limit, 
        not null, not empty, etc"""
    @parameterized.expand([
        ("Age", "Age should not contain null values"),
        ("Age", "Age should not be empty"),
        ("Name", "Name should not contain null values"),
        ("Name", "Name should not be empty"),
        ("Email", "Email should not contain null values"),
        ("Email", "Email should not be empty"),
        ("Subscriber", "Subscriber should not contain null values"),
        ("Subscriber", "Subscriber should not be empty")
    ])
    def test_constraint_validation(self, column, message):
        self.assertFalse(self.data[column].isnull().any(), message)
        self.assertFalse(self.data[column].eq('').any(), message)

    """Checks compliance with a data format, structure or schema e.g.: primary key, foreign key, data name,
            column name"""
    @parameterized.expand([
        (['Name', 'Age', 'Email', 'Subscriber'], "Required columns are missing")
    ])
    def test_structured_validation(self, required_columns, message):
        self.assertTrue(set(required_columns).issubset(self.data.columns), message)

    """Checks data style e.g.: date masks, currency, etc."""
    @parameterized.expand([
        (['example.com'], "Invalid email domain found")
    ])
    def test_consistency_validation(self, criterion, message):
        valid_email_domains = criterion
        email_domains = self.data['Email'].str.split('@').str[1]
        self.assertTrue(email_domains.isin(valid_email_domains).all(), message)

    """Checks that the classifications adhere to 'Yes' or 'No'."""
    @parameterized.expand([
        (['Yes', 'No'], "Invalid values found in 'Subscriber'")
    ])
    def test_code_validation(self, valid_values, message):
        self.assertTrue(self.data['Subscriber'].isin(valid_values).all(), message)


if __name__ == '__main__':
    unittest.main()
