Framework to help me as a QA Engineer to check the data quality of a dataset.

To practice this I used a data-driven approach to run the test class using a csv file with different data
and also a structure of 5 data checks (type, constraint, structured, consistency and code)

# Data Validation Test Suite

A Python unittest-based test suite for validating data quality in CSV datasets.

## Overview

This test suite is designed to get fast feedback on data quality in CSV datasets.
It performs various checks, including data type validation, constraint validation,
structured validation, consistency validation and code validation.

## Installation

To run the tests, you need Python 3.x and the following dependencies:

```bash
pip install pandas parameterized
```

## Usage
Clone the repository.
Run the tests using unittest:

```bash
python -m unittest -v test_data_validation.py
```

## Tests
### Data Type Validation
- Checks that the data in each field, column, list, range or file corresponds to the correct type and format e.g.: int, str, bool, etc.

### Constraint Validation
- Checks that the data meets valid value ranges or expectations e.g.: age field has a valid age limit, not null, not empty, etc.

### Structured Validation
- Checks compliance with a data format, structure or schema e.g.: primary key, foreign key, data name, column name

### Consistency Validation
- Checks data style e.g.: date masks, currency, etc.

### Code Validation
- Checks that the classifications adhere to 'Yes' or 'No', '0' or '1', etc.

## References

- [Python unittest Library Documentation](https://docs.python.org/3/library/unittest.html): Official documentation for the Python unittest library.
- [Unit Testing in Python](https://www.dataquest.io/blog/unit-tests-python/): A comprehensive guide to unit testing in Python.
- [Data Validation - TechTarget](https://www.techtarget.com/searchdatamanagement/definition/data-validation): Information about data validation on TechTarget.

## License
This project is licensed under the MIT License - see the LICENSE file for details.