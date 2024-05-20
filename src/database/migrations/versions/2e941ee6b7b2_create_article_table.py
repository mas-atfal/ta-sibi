"""create article table

Revision ID: 2e941ee6b7b2
Revises: 08ac96511afe
Create Date: 2024-05-20 09:55:36.693642

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2e941ee6b7b2'
down_revision: Union[str, None] = '08ac96511afe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('articles', 
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('user_id', sa.BigInteger, nullable=False),
        sa.Column('category_id', sa.BigInteger, nullable=False),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('slug_title', sa.CHAR(16), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('status', sa.Enum('published', 'draft'), nullable=False),
        sa.Column('image', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('deleted_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_articles')),
    )
    
    op.create_foreign_key('fk_articles_users', 'articles', 'users', ['user_id'], ['id'])
    op.create_foreign_key('fk_articles_categories', 'articles', 'categories', ['category_id'], ['id'])


def downgrade() -> None:
    pass
