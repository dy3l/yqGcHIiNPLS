import csv
from datetime import date

from pydantic import BaseModel, conint, constr


class Company(BaseModel):
    id: constr(regex=r"[a-z0-9-+]+")
    name: constr(min_length=3, max_length=21)
    description: str
    website: str
    facebook: str
    instagram: str
    linkedin: str
    twitter: str
    founded_date: conint(ge=2010, le=date.today().year)
    number_of_employees: constr(regex=r"(1-10|11-50|TODO)")
    headquarters: constr(regex=r"Bouskoura|Casablanca|Marrakesh|Rabat|Tangier|TODO")


def test_companies():
    with open("data/companies.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        companies = list(reader)
    for company in companies:
        Company(
            id=company["id"],
            name=company["name"],
            description=company["description"],
            website=company["website"],
            facebook=company["facebook"],
            instagram=company["instagram"],
            linkedin=company["linkedin"],
            twitter=company["twitter"],
            founded_date=company["founded_date"],
            number_of_employees=company["number_of_employees"],
            headquarters=company["headquarters"],
        )


test_companies()

