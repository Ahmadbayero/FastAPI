"""add title column to posts table

Revision ID: 377d09024543
Revises: b29968f287c7
Create Date: 2022-02-03 12:21:28.545210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '377d09024543'
down_revision = 'b29968f287c7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
