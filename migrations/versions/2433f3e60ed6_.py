"""empty message

Revision ID: 2433f3e60ed6
Revises: 
Create Date: 2022-12-22 19:13:48.691139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2433f3e60ed6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('table_private_key',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('table_id', sa.Integer(), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('private_key', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['table_id'], ['table.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('table_private_key')
    # ### end Alembic commands ###
