"""empty message

Revision ID: 111ff4fb3159
Revises: 
Create Date: 2022-08-26 22:39:39.542194

"""
from alembic import op
import sqlalchemy as sa



revision = '111ff4fb3159'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('terrain', sa.String(length=50), nullable=False),
    sa.Column('climate', sa.String(length=50), nullable=False),
    sa.Column('orbit_period', sa.Integer(), nullable=False),
    sa.Column('orbit_rotation', sa.Integer(), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('url_image', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('url_image'),
    sa.UniqueConstraint('url_image')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('last_name', sa.String(length=30), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=False),
    sa.Column('creation_date', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username'),
    sa.UniqueConstraint('username')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('birth_date', sa.String(length=10), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=50), nullable=False),
    sa.Column('eye_color', sa.String(length=50), nullable=False),
    sa.Column('skin_color', sa.String(length=50), nullable=False),
    sa.Column('url_image', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('url_image'),
    sa.UniqueConstraint('url_image')
    )
    op.create_table('starship',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('model', sa.Integer(), nullable=True),
    sa.Column('manufacturer', sa.String(length=120), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('crew', sa.Integer(), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('cargo_capacity', sa.Integer(), nullable=True),
    sa.Column('created', sa.String(length=70), nullable=True),
    sa.Column('consumables', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('vehicle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('vehicle_class', sa.String(length=100), nullable=True),
    sa.Column('passengers', sa.Integer(), nullable=True),
    sa.Column('max_speed', sa.Integer(), nullable=True),
    sa.Column('consumables', sa.Integer(), nullable=True),
    sa.Column('url_image', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('description'),
    sa.UniqueConstraint('url_image'),
    sa.UniqueConstraint('url_image')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.Column('starship_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['starship_id'], ['starship.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )



def downgrade():

    op.drop_table('favorite')
    op.drop_table('vehicle')
    op.drop_table('starship')
    op.drop_table('character')
    op.drop_table('user')
    op.drop_table('planet')

