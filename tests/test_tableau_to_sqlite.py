from click.testing import CliRunner
from tableau_to_sqlite.cli import cli
import pathlib
import sqlite3
import vcr

fixtures = pathlib.Path(__file__).parent / "fixtures"


@vcr.use_cassette(str(fixtures / "cassette.yml"))
def test_run(tmpdir):
    runner = CliRunner()
    db_path = str(tmpdir / "tableau.db")
    result = runner.invoke(
        cli,
        [
            db_path,
            "https://results.mo.gov/t/COVID19/views/VaccinationsDashboard/Vaccinations",
        ],
    )
    assert result.exit_code == 0
    db = sqlite3.connect(db_path)
    tables = db.execute(
        'select name from sqlite_master where type = "table"'
    ).fetchall()
    assert tables == [
        ("% Share State",),
        ("Age - % Complete",),
        ("By Date",),
        ("County - Table",),
        ("Dashboard Date",),
        ("Ethnicity - % Complete",),
        ("Num Vaccinations",),
        ("Num Vax Dose 1",),
        ("Num Vax Dose 2",),
        ("Num Vax Last 7",),
        ("Race - % Complete",),
        ("Sex - % Complete",),
        ("v2 County Map - % of Pop",),
    ]
