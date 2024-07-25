# Pokémon API

This project provides a REST API to serve a list of Pokémon using FastAPI and PostgreSQL.


### Prerequisites

- Python 3.8+
- PostgreSQL
- Git
- An IDE or text editor (e.g., VSCode, Pycharm)



## Setup Instructions

1. Clone the repository:
   ```sh
   git clone <https://github.com/SujishMaharjan/pokemon-api.git>
   cd pokemon_api


2. Create a virtual emvironment and activate it.
    python -m venv env
    env\Scripts\activate

3. Install the required packages.
    pip install -r requirements.txt

4. Edit .env file with your database configuration.
    DATABASE_URL=postgresql+asyncpg://username:password@localhost/database_name

5. Initialize Alembic for database migrations.
    alembic init alembic

6. Edit 'alembic.ini' to set the database URL.
    sqlalchemy.url = postgresql+asyncpg://username:password@localhost/database_name

7. Create and apply migrations.
    alembic revision --autogenerate -m "Create pokemons table"
    alembic upgrade head

8. Populate the database with Pokemon data:
    python populate_db.py

9. Run the FastAPI application
    uvicorn main:app --reload

10. Test the FastAPI

    http://127.0.0.1:8000/api/v1/pokemons
    To see server list of pokemons

    http://127.0.0.1:8000/api/v1/pokemons?name=pokemon_name
    To filter the pokemon by name

    http://127.0.0.1:8000/api/v1/pokemons?type=pokemon_type
    To filter the pokemon by its type

    http://127.0.0.1:8000/api/v1/pokemons?name=pokemon_name&type=pokemon_type
    To filter the pokemon by name and its type