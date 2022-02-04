"""generate votes

Revision ID: 3b930e674142
Revises: e37d16060073
Create Date: 2022-02-03 13:06:03.732685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b930e674142'
down_revision = 'e37d16060073'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('users_email_key', 'users', type_='unique')
    op.create_unique_constraint(None, 'users', ['password'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.create_unique_constraint('users_email_key', 'users', ['email'])
    # ### end Alembic commands ###