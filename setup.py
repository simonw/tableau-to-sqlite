from setuptools import setup
import os

VERSION = "0.2.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="tableau-to-sqlite",
    description="Fetch data from Tableau into a SQLite database",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/tableau-to-sqlite",
    project_urls={
        "Issues": "https://github.com/simonw/tableau-to-sqlite/issues",
        "CI": "https://github.com/simonw/tableau-to-sqlite/actions",
        "Changelog": "https://github.com/simonw/tableau-to-sqlite/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["tableau_to_sqlite"],
    entry_points="""
        [console_scripts]
        tableau-to-sqlite=tableau_to_sqlite.cli:cli
    """,
    install_requires=["click", "TableauScraper==0.1.2"],
    extras_require={"test": ["pytest", "vcrpy"]},
    tests_require=["tableau-to-sqlite[test]"],
    python_requires=">=3.6",
)
