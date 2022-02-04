"""create votes table

Revision ID: 1a23c2900c6b
Revises: 24f499cde94b
Create Date: 2022-02-04 20:57:25.738919

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a23c2900c6b'
down_revision = '24f499cde94b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes', sa.Column('post_id', sa.Integer(), sa.ForeignKey('posts.id', ondelete='CASCADE'), primary_key=True), sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE'), primary_key=True))
    pass


def downgrade():
    op.drop_table('votes')
    pass
