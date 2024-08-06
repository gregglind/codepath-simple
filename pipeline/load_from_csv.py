from config import RAWDATADIR
import polars as pl
from models import get_engine, RegionalMetrics

# in the real one we would loop over all files, taken in as a pathlib.glob
def transform(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.col("region")
        .str.split_exact("_", 1)
        .struct.rename_fields(["country", "area"])
        .alias("fields")
    ).unnest("fields")

# to do, could do group by and agg here, but will do it instead in the db, for more EDA opportunity.
def aggregate(df: pl.DataFrame) -> pl.DataFrame:
    return df


def insert_to_db(df: pl.DataFrame) -> None:
    to_insert_regional = [
        RegionalMetrics(
            country_code=row["country_code"],
            region=row["country_code"],
            year=row["country_code"],
            quarter=row["country_code"],
            level=row["country_code"],
        )
        for row in df.rows()
    ]

    # Aggregate to yearly, using polars
    grouped = df.group_by(['country_code','region', 'quarter'],maintain_order=True).mean()
    to_insert_aggregated = [
        # make a model for each grouped at the aggreation level of annual
    ]

    with get_engine().connect() as conn:
        # do the multinsert of the RegionalMetrics




def task():
    pass


df = None
print(RAWDATADIR)
for fn in RAWDATADIR.glob("regional_data_eef480e.csv"):
    print(fn)
    df = pl.read_csv(fn)
    df = transform(df)
    df = aggregate(df)
    insert_to_db(df)
    # country, year, cereal_yield


if __name__ == "__main__":
    task()
