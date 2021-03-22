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

        tableau-to-sqlite tableau.db OregonCOVID-19VaccineProviderEnrollment/COVID-19VaccineProviderEnrollment

    You can also pass a full URL to a Tableau dashboard, for example:

        tableau-to-sqlite tableau.db https://results.mo.gov/t/COVID19/views/VaccinationsDashboard/Vaccinations
    """
    for view in tableau_views:
        if not (view.startswith("http://") or view.startswith("https://")):
            url = "https://public.tableau.com/views/{}".format(view)
        else:
            url = view
        ts = TableauScraper()
        ts.loads(url)
        workboop = ts.getWorkbook()
        conn = sqlite3.connect(str(db_path))
        for worksheet in workboop.worksheets:
            worksheet.data.to_sql(fix_name(worksheet.name), conn)


def fix_name(name):
    return name.replace("'", "").replace('"', "")
