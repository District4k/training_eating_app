"""Removeing not used models

Revision ID: 511fb7bb0c5b
Revises: 48c9c2e68296
Create Date: 2024-12-13 07:22:26.978783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '511fb7bb0c5b'
down_revision: Union[str, None] = '48c9c2e68296'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
