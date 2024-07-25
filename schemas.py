from typing import List
from pydantic import BaseModel

class PokemonBase(BaseModel):
    name: str
    image_url: str
    types: List[str]

class PokemonCreate(PokemonBase):
    pass

class Pokemon(PokemonBase):
    id: int

    class Config:
        orm_mode = True
