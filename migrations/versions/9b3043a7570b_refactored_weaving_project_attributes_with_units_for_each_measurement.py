"""empty message

Revision ID: 9b3043a7570b
Revises: 85d9ebe15f07
Create Date: 2022-05-04 10:49:06.400362

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b3043a7570b'
down_revision = '85d9ebe15f07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('width_in_reed_unit', sa.String(length=2), nullable=True))
    op.add_column('projects', sa.Column('warped_length_unit', sa.String(length=2), nullable=True))
    op.add_column('projects', sa.Column('finished_length_unit', sa.String(length=2), nullable=True))
    op.add_column('projects', sa.Column('finished_width_unit', sa.String(length=2), nullable=True))
    op.drop_column('projects', 'width_unit')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('projects', sa.Column('width_unit', sa.VARCHAR(length=2), autoincrement=False, nullable=True))
    op.drop_column('projects', 'finished_width_unit')
    op.drop_column('projects', 'finished_length_unit')
    op.drop_column('projects', 'warped_length_unit')
    op.drop_column('projects', 'width_in_reed_unit')
    # ### end Alembic commands ###
