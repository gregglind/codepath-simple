from config import RAWDATADIR
import polars as pl


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
    return None


df = None
print(RAWDATADIR)
for fn in RAWDATADIR.glob("regional_data_eef480e.csv"):
    print(fn)
    df = pl.read_csv(fn)
    df = transform(df)
    df = aggregate(df)
    insert_to_db(df)
    # country, year, cereal_yield
