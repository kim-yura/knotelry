"""empty message

Revision ID: f9a7e47d5958
Revises: dfd8cb52356b
Create Date: 2022-05-16 11:46:40.567255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9a7e47d5958'
down_revision = 'dfd8cb52356b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stash', sa.Column('fabric_height', sa.Integer(), nullable=True))
    op.add_column('stash', sa.Column('fabric_height_unit', sa.String(length=2), nullable=True))
    op.add_column('stash', sa.Column('aida_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stash', 'aida_count')
    op.drop_column('stash', 'fabric_height_unit')
    op.drop_column('stash', 'fabric_height')
    # ### end Alembic commands ###
