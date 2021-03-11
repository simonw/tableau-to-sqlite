# tableau-to-sqlite

[![PyPI](https://img.shields.io/pypi/v/tableau-to-sqlite.svg)](https://pypi.org/project/tableau-to-sqlite/)
[![Changelog](https://img.shields.io/github/v/release/simonw/tableau-to-sqlite?include_prereleases&label=changelog)](https://github.com/simonw/tableau-to-sqlite/releases)
[![Tests](https://github.com/simonw/tableau-to-sqlite/workflows/Test/badge.svg)](https://github.com/simonw/tableau-to-sqlite/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/tableau-to-sqlite/blob/master/LICENSE)

Fetch data from Tableau into a SQLite database. A wrapper around [TableauScraper](https://github.com/bertrandmartel/tableau-scraping/).

## Installation

Install this tool using `pip`:

    $ pip install tableau-to-sqlite

## Usage

You need to know the name of the Tableau view you want to import. This will be two strings separated by a `/` symbol - something like this:

    OregonCOVID-19VaccineProviderEnrollment/COVID-19VaccineProviderEnrollment

Now run the tool like this:

    tableau-to-sqlite tableau.db \
        OregonCOVID-19VaccineProviderEnrollment/COVID-19VaccineProviderEnrollment

This will create a SQLite database called `tableau.db` containing one table for each of the worksheepts in the view.

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd tableau-to-sqlite
    python -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and tests:

    pip install -e '.[test]'

To run the tests:

    pytest
