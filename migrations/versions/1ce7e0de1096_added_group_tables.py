"""empty message

Revision ID: 1ce7e0de1096
Revises: aa62f8366190
Create Date: 2022-05-19 12:01:23.813701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ce7e0de1096'
down_revision = 'aa62f8366190'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('craft_types', sa.String(length=50), nullable=True),
    sa.Column('country', sa.String(length=2), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.Column('moderator_ids', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group_memberships',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group_memberships')
    op.drop_table('groups')
    # ### end Alembic commands ###
