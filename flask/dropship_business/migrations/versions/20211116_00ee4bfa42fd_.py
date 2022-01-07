"""empty message

Revision ID: 00ee4bfa42fd
Revises: 1f03cf1e6c01
Create Date: 2021-11-16 21:52:08.734846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00ee4bfa42fd'
down_revision = '1f03cf1e6c01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.drop_constraint('accounts_id_fkey', 'accounts', type_='foreignkey')
    op.create_foreign_key(None, 'accounts', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'accounts', type_='foreignkey')
    op.create_foreign_key('accounts_id_fkey', 'accounts', 'customers', ['id'], ['id'])
    op.drop_column('accounts', 'customer_id')
    # ### end Alembic commands ###
