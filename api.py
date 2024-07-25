from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
import crud, schemas
from database import get_db

router = APIRouter()

@router.get("/pokemons", response_model=List[schemas.Pokemon])
async def read_pokemons(
    name: Optional[str] = Query(None, description="Filter by name"),
    type: Optional[str] = Query(None, description="Filter by type"),
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db)
):
    pokemons = await crud.get_pokemons(db, name=name, type=type, skip=skip, limit=limit)
    return pokemons
