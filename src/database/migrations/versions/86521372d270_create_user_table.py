"""create user table

Revision ID: 86521372d270
Revises: 
Create Date: 2024-04-25 07:12:33.699832

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86521372d270'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users', 
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('users')
