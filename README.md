# Hakai CKAN Records Checks

This repository contains a set of tests that can be executed on each CKAN record available on the Hakai Institute CKAN catalogue. These tests are designed specifically for the Hakai Institute CKAN catalogue.

The result is summarized via the github page:
https://hakaiinstitute.github.io/hakai-ckan-records-checks/

## Purpose

The purpose of this repository is to ensure the quality and integrity of the CKAN records in the Hakai Institute CKAN catalogue. By running these tests, we can identify any issues or inconsistencies in the data and take appropriate actions to resolve them.

## Getting Started

To get started with running the tests, follow these steps:

1. Clone this repository to your local machine.
2. Install poetry
3. Install the necessary dependencies (ideally within an environment). 4. We recommend to use poetry:
   ```console
   poetry install
   ```
4. Execute the tests:
   ```console
   poetry run hakai_ckan_records_checks -c https://catalogue.hakai.org --cache
   ```
5. Render pages
   ```console
   poetry run mkdocs serve
   ```

## Test Categories

The tests in this repository are organized into the following categories:

1. Data completeness: These tests check if all the required fields in the CKAN records are populated.
2. Data consistency: These tests verify the consistency of data across different CKAN records.
3. Data accuracy: These tests validate the accuracy of specific data fields in the CKAN records.
4. Data format: These tests ensure that the data in the CKAN records adhere to the specified format.

## Contributing

Contributions to this repository are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This repository is licensed under the [MIT License](LICENSE).
