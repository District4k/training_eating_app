"""cjangge

Revision ID: 48c9c2e68296
Revises: 7e968f8250d1
Create Date: 2024-12-12 12:13:56.554634

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '48c9c2e68296'
down_revision: Union[str, None] = '7e968f8250d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
