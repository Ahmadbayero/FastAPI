"""add forienKey to posts

Revision ID: 38036d0c53df
Revises: 47020fd690e4
Create Date: 2022-02-03 12:40:57.421340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38036d0c53df'
down_revision = '47020fd690e4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fkey', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('posts_users_fkey', table_name='posts')
    pass
