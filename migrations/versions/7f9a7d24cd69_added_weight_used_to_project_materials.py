"""empty message

Revision ID: 7f9a7d24cd69
Revises: d4bed2e4bfe2
Create Date: 2022-04-15 15:14:18.665834

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f9a7d24cd69'
down_revision = 'd4bed2e4bfe2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_materials', sa.Column('weight_used', sa.Float(), nullable=True))
    op.add_column('project_materials', sa.Column('weight_unit', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_materials', 'weight_unit')
    op.drop_column('project_materials', 'weight_used')
    # ### end Alembic commands ###
