"""add remaining columns to posts

Revision ID: e37d16060073
Revises: 38036d0c53df
Create Date: 2022-02-03 12:52:14.102508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e37d16060073'
down_revision = '38036d0c53df'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='True'))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')))
    pass


def downgrade():
    op.drop_column('posts', column_name='published')
    op.drop_column('posts', column_name='created_at')
    pass
