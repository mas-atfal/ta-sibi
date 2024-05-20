"""create category table

Revision ID: 08ac96511afe
Revises: 86521372d270
Create Date: 2024-05-20 09:54:20.749977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08ac96511afe'
down_revision: Union[str, None] = '86521372d270'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('categories', 
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('parent_id', sa.BigInteger, nullable=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('slug_name', sa.CHAR(16), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_categories')),
    )

def downgrade() -> None:
    op.drop_table('categories')
