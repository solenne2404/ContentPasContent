"""empty message

Revision ID: a9dca4186fae
Revises: 35626f2f537a
Create Date: 2019-11-21 23:26:19.666957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9dca4186fae'
down_revision = '35626f2f537a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('FK__user__promo',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('promo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['promo_id'], ['promo.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'promo_id')
    )
    op.create_index(op.f('ix_promo_name'), 'promo', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_promo_name'), table_name='promo')
    op.drop_table('FK__user__promo')
    # ### end Alembic commands ###
