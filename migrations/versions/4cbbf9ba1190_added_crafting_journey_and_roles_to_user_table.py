"""empty message

Revision ID: 4cbbf9ba1190
Revises: 2fa3706befd3
Create Date: 2022-04-27 10:49:35.403259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cbbf9ba1190'
down_revision = '2fa3706befd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('crafting_journey', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('roles', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'roles')
    op.drop_column('users', 'crafting_journey')
    # ### end Alembic commands ###
