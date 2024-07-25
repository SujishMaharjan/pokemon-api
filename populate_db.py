import asyncio
import requests
from sqlalchemy.ext.asyncio import AsyncSession
from database import async_session, engine
from models import Base, Pokemon
from crud import create_pokemon
from schemas import PokemonCreate

POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon?limit=100"

async def fetch_pokemon_data():
    response = requests.get(POKEAPI_URL)
    pokemons = response.json().get("results", [])
    return pokemons

async def fetch_pokemon_details(url):
    response = requests.get(url)
    data = response.json()
    return {
        "name": data["name"],
        "image_url": data["sprites"]["front_default"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

async def populate_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        pokemons = await fetch_pokemon_data()
        for pokemon in pokemons:
            details = await fetch_pokemon_details(pokemon["url"])
            await create_pokemon(session, PokemonCreate(**details))

if __name__ == "__main__":
    asyncio.run(populate_database())
