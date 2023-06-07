"""empty message

Revision ID: 9b831e7b30b5
Revises: 6647b6f09791
Create Date: 2023-06-07 11:54:28.259264

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9b831e7b30b5'
down_revision = '6647b6f09791'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'currency',
               existing_type=postgresql.ENUM('sum', 'dollar', name='currencyenum'),
               type_=sa.String(),
               existing_nullable=True,)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'currency',
               existing_type=sa.String(),
               type_=postgresql.ENUM('sum', 'dollar', name='currencyenum'),
               existing_nullable=True)
    # ### end Alembic commands ###
