"""term in terms

Revision ID: 683875afc4d3
Revises: accd8546a3a9
Create Date: 2024-12-11 14:05:53.894342

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '683875afc4d3'
down_revision: Union[str, None] = 'accd8546a3a9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('terms', sa.Boolean(), nullable=False))
    op.drop_column('user_model', 'term')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_model', sa.Column('term', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.drop_column('user_model', 'terms')
    # ### end Alembic commands ###
