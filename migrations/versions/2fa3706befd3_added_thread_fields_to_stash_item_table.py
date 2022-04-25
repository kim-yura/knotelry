"""empty message

Revision ID: 2fa3706befd3
Revises: 3fd68c9e6edc
Create Date: 2022-04-25 12:01:40.465367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fa3706befd3'
down_revision = '3fd68c9e6edc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('stash', sa.Column('length_per_bobbin', sa.Float(), nullable=True))
    op.add_column('stash', sa.Column('bobbins_stashed', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stash', 'bobbins_stashed')
    op.drop_column('stash', 'length_per_bobbin')
    # ### end Alembic commands ###