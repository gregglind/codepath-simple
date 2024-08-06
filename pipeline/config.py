import pathlib
print(__file__)

DBURL = (pathlib.Path(__file__) / "../../db/db.sqlite").resolve()
DATADIR = (pathlib.Path(__file__) / "../../data").resolve()
RAWDATADIR = (pathlib.Path(__file__) / "../../data/raw").resolve()
EXTERNALAPI = ""
