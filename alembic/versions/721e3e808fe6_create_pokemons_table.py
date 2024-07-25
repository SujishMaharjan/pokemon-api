"""Create pokemons table

Revision ID: 721e3e808fe6
Revises: 59fbf53b79c9
Create Date: 2024-07-24 15:41:22.335841

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '721e3e808fe6'
down_revision: Union[str, None] = '59fbf53b79c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
