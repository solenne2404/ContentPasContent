"""promo table and fkuserpromo

Revision ID: 35626f2f537a
Revises: d7c76e399df0
Create Date: 2019-11-18 22:32:28.776764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35626f2f537a'
down_revision = 'd7c76e399df0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('promo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_promo_name'), 'promo', ['name'], unique=True)
    op.create_table('FK__user__promo',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('promo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['promo_id'], ['promo.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'promo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('FK__user__promo')
    op.drop_index(op.f('ix_promo_name'), table_name='promo')
    op.drop_table('promo')
    # ### end Alembic commands ###