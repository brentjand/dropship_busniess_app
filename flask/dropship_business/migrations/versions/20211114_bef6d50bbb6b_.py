"""empty message

Revision ID: bef6d50bbb6b
Revises: f29d3f030946
Create Date: 2021-11-14 13:46:00.265040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bef6d50bbb6b'
down_revision = 'f29d3f030946'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contracted_brands',
    sa.Column('brand_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('brand_id', 'product_id')
    )
    op.drop_table('brand_contracts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('brand_contracts',
    sa.Column('brand_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['brand_id'], ['brands.id'], name='brand_contracts_brand_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='brand_contracts_product_id_fkey'),
    sa.PrimaryKeyConstraint('brand_id', 'product_id', name='brand_contracts_pkey')
    )
    op.drop_table('contracted_brands')
    # ### end Alembic commands ###
