# Django Template - DRF Django Rest Framwork
# FastApi
# Flask

#####################################
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Country(BaseModel):
    country_id: int = Field(alias='id')
    name: str
    capital: str
    area: int

countries = [
    Country(id=1, name="Thailand", capital="Bangkok", area=513120),
    Country(id=2, name="Australia", capital="Canberra", area=7617930),
    Country(id=3, name="Egypt", capital="Cairo", area=1010408),
]

@app.get('/')
def root():
    return 'salam chetori\n'

@app.get('/countries')
def get_countries():
    return countries

@app.post('/countries', status_code=201)
def add_country(country: Country):
    countries.append(country)
    return countries

# FastApi - Uvicorn
# Php Apache
# Django guvicorn
