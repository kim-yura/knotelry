"""empty message

Revision ID: 55feb17be620
Revises: 1ce7e0de1096
Create Date: 2022-05-23 11:12:56.176505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55feb17be620'
down_revision = '1ce7e0de1096'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('group_memberships', sa.Column('created_at', sa.DateTime(), nullable=False))
    op.add_column('groups', sa.Column('created_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('groups', 'created_at')
    op.drop_column('group_memberships', 'created_at')
    # ### end Alembic commands ###
