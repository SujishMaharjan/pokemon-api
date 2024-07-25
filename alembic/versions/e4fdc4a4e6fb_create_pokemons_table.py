"""Create pokemons table

Revision ID: e4fdc4a4e6fb
Revises: 721e3e808fe6
Create Date: 2024-07-25 06:27:35.238284

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e4fdc4a4e6fb'
down_revision: Union[str, None] = '721e3e808fe6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
