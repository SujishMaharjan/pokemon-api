from typing import List, Optional
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, text
from models import Pokemon

async def get_pokemons(
    db: AsyncSession,
    name: Optional[str] = None,
    type: Optional[str] = None,
    skip: int = 0,
    limit: int = 100
) -> List[Pokemon]:
    try:
        query = select(Pokemon).offset(skip).limit(limit)

        # Filter by name if provided
        if name:
            query = query.filter(Pokemon.name.ilike(f"%{name}%"))

        # Filter by type if provided using PostgreSQL array operations
        if type:
            query = query.filter(text(f":type = ANY(types)")).params(type=type)

        result = await db.execute(query)
        return result.scalars().all()
    except Exception as e:
        # Log the exception for debugging purposes
        print(f"Error fetching pokemons: {str(e)}")
        raise Exception(f"Error fetching pokemons: {str(e)}")
