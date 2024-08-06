# CodePath project 

## Problem Analysis

Incoming data exists at 4 different resolutions on two different axes

* Geography
* Time

### Data Resolutions

* Country (Eternal), sourced from `db`, including
    * country_id
    * country_code
    * total_land_area
    * Country + Year.

* Country > Region +  Year > Quarter, sourced from "Regional" csvs, including
    * cereal_yield 

* Country > Region > Person +  Year > Quarter > Timestamp, source from the Survey responses

The final expected report is at the Country x Year level.  The final report requires both rollup (individuals > regions and repeating information.

## File Structure

* "Common" library for db connections and models
* pipeline/ for all ETL tasks.  Each task has the same structure.
* data/ for storing data, modeled after the Cookiecutter Data Science
* db/ location of the db

### Models

See `models.py` for partial work.

* Regional.  Including a 'AggregationLevelEnum' to enable both regional-quarterly and annual summarizations to be in the same table.
* TBD:  annual and eternal



### Simplification / Future expansions.

1. No containerization.  
2. Packaging as files (rather than proper python packages)
    * Each ETL process (CSV, external api, ) should be in a package
    * common should be package
3. Didn't work on the dashboard api.  
4. No alembic or migrations.  
5. No logging or tracing.
6. No orchestration. 