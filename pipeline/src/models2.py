from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


def Common():
    print("This is running from common")

"""
Final reports want things by *region*
"""


SURVEY = """
{
  "country": "string",
  "year": 0,
  "surveys": [
    {
      "survey_time": "string",
      "region": "string",
      "female": true,
      "age": 0,
      "literate": true,
      "access_to_electricity": true,
      "access_to_improved_water_sources": true,
      "access_to_improved_sanitation": true,
      "completed_school": true,
      "employed": true,
      "avg_protein_per_day": 0,
      "caloric_energy_from_cereals_roots_tubers": 0
    }
  ]
}

Country Year
['survey_time', 'region', 'female', 'age', 'literate', 'access_to_electricity', 'access_to_improved_water_sources', 'access_to_improved_sanitation', 'completed_school', 'employed', 'avg_protein_per_day', 'caloric_energy_from_cereals_roots_tubers']

survey_time
region
female
age
literate
access_to_electricity
access_to_improved_water_sources
access_to_improved_sanitation
completed_school
employed
avg_protein_per_day
caloric_energy_from_cereals_roots_tubers

"""


CSV = """
csv
region
quarter
cereal_yield
agricultural_land_area
imports_of_goods_and_services
co2_emissions
forest_area
"""


FINAL_REPORT = """
country_code  
year
total_land_area
total_population
rural_population
urban_population
net_oda_received_per_capita
gross_domestic_product_per_capita_ppp
tax_revenue_share_gdp
military_expenditure_share_gdp
cereal_yield
agricultural_land_area
imports_of_goods_and_services
co2_emissions
forest_area
adult_literacy_rate
access_to_electricity
access_to_improved_water_sources
access_to_improved_sanitation
school_enrollment_rate_total
unemployment_rate
avg_supply_of_protein_of_animal_origin
caloric_energy_from_cereals_roots_tubers
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base


PROJECTROOT = ""
DBLOCATION = ""


def create_db():
    engine = create_engine("sqlite://")
    Modelbase.metadata.create_all(engine)  # should be Alembic up / downs


Base = declarative_base()


class Modelbase(Base):
    # in case we want to add helper methods
    pass


class CountryStatic(Modelbase):
    # pk
    country_code
    coun

    # traits
    total_land_area

    pass


class CountryYearMetrics(Modelbase):
    # pk
    country_code
    year

    # facts
    total_population
    rural_population
    urban_population
    net_oda_received_per_capita
    gross_domestic_product_per_capita_ppp
    tax_revenue_share_gdp
    military_expenditure_share_gdp
    pass


class CountryRegionQuarterMetrics(Modelbase):
    # pk
    country_code
    year
    region

    #
    cereal_yield  # mean
    agricultural_land_area  # mean
    imports_of_goods_and_services

    forest_area  # regional

    co2_emissions
    adult_literacy_rate
    access_to_electricity
    access_to_improved_water_sources
    access_to_improved_sanitation
    school_enrollment_rate_total
    unemployment_rate
    avg_supply_of_protein_of_animal_origin
    caloric_energy_from_cereals_roots_tubers
