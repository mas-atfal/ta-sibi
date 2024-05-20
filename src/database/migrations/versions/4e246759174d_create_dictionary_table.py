"""create dictionary table

Revision ID: 4e246759174d
Revises: 2e941ee6b7b2
Create Date: 2024-05-20 09:55:43.618164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4e246759174d'
down_revision: Union[str, None] = '2e941ee6b7b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('dictionaries', 
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('slug_name', sa.CHAR(16), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('image', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_dictionaries')),
    )


def downgrade() -> None:
    op.drop_table('dictionaries')
