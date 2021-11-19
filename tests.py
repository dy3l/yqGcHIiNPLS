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


class Person(BaseModel):
    id: constr(regex=r"[a-z-]+")
    name: str


class Role(BaseModel):
    person_id: constr(regex=r"[a-z-]+")
    company_id: constr(regex=r"[a-z-]+")
    role: constr(regex=r"(founder|co-founder)")


class Investor(BaseModel):
    id: constr(regex=r"[a-z-]+")
    name: constr(min_length=3, max_length=21)
    description: constr()
    website: str
    founded_date: str
    headquarters: constr(regex=r"Casablanca|Rabat|TODO")


class Investment(BaseModel):
    company_id: constr(regex=r"[a-z-]+")
    investor_id: constr(regex=r"[a-z-]+")
    amount: conint(ge=3000000, le=12000000)
    currency: constr(regex=r"MAD")
    type: constr(regex=r"(seed)")
    raised_date: date


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


def test_people():
    with open("data/people.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        people = list(reader)
    for person in people:
        Person(
            id=person["id"],
            name=person["name"],
        )


def test_roles():
    with open("data/roles.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        roles = list(reader)
    for role in roles:
        Role(
            person_id=role["person_id"],
            company_id=role["company_id"],
            role=role["role"],
        )


def test_investments():
    with open("data/investments.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        investments = list(reader)
    for investment in investments:
        Investment(
            company_id=investment["company_id"],
            investor_id=investment["investor_id"],
            amount=investment["amount"],
            currency=investment["currency"],
            type=investment["type"],
            raised_date=investment["raised_date"],
        )


def test_investors():
    with open("data/investors.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=",")
        investors = list(reader)
    for investor in investors:
        Investor(
            id=investor["id"],
            name=investor["name"],
            description=investor["description"],
            website=investor["website"],
            founded_date=investor["founded_date"],
            headquarters=investor["headquarters"],
        )

test_companies()
test_people()
test_roles()
test_investments()
test_investors()