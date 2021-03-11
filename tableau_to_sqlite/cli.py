import click
from click.decorators import version_option
from tableauscraper import TableauScraper
import sqlite3


@click.command()
@click.argument(
    "db_path",
    type=click.Path(file_okay=True, dir_okay=False, allow_dash=False),
    required=True,
)
@click.argument("tableau_views", nargs=-1)
@version_option()
def cli(db_path, tableau_views):
    """Fetch data from Tableau into a SQLite database

    Pass this command a SQLite databsae file and one or more
    Tableau views, where a Tableau view looks like this:

        OregonCOVID-19VaccineProviderEnrollment/COVID-19VaccineProviderEnrollment

    For example:

        tableau-to-sqlite tableau.db \
            OregonCOVID-19VaccineProviderEnrollment/COVID-19VaccineProviderEnrollment
    """
    for view in tableau_views:
        url = "https://public.tableau.com/views/{}".format(view)
        ts = TableauScraper()
        ts.loads(url)
        dashboard = ts.getDashboard()
        conn = sqlite3.connect(str(db_path))
        for worksheet in dashboard.worksheets:
            worksheet.data.to_sql(fix_name(worksheet.name), conn)


def fix_name(name):
    return name.replace("'", "").replace('"', "")
