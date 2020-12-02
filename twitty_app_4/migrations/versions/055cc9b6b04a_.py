"""empty message

Revision ID: 055cc9b6b04a
Revises: 
Create Date: 2020-12-02 18:46:45.551652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '055cc9b6b04a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tweet', sa.Column('username', sa.String(), nullable=True))
    op.alter_column('user', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('tweet', 'username')
    # ### end Alembic commands ###
