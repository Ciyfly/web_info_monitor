"""empty message

Revision ID: aee0126a0ab6
Revises: 047814a533cd
Create Date: 2019-09-03 19:38:03.165503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aee0126a0ab6'
down_revision = '047814a533cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_domain',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('domain_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['domain_id'], ['domain.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'domain_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_domain')
    # ### end Alembic commands ###
