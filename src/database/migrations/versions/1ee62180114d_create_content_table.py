"""create content table

Revision ID: 1ee62180114d
Revises: 4e246759174d
Create Date: 2024-05-20 09:55:55.058288

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1ee62180114d'
down_revision: Union[str, None] = '4e246759174d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('contents', 
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('app_title', sa.String(255), nullable=False),
        sa.Column('app_description', sa.Text(), nullable=False),
        sa.Column('app_logo', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_contents')),
    )


def downgrade() -> None:
    op.drop_table('contents')
