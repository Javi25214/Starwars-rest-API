"""empty message

Revision ID: 207c276f6fdc
Revises: 111ff4fb3159
Create Date: 2022-08-31 21:32:34.794797

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


revision = '207c276f6fdc'
down_revision = '111ff4fb3159'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('character', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('character', 'gender',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('character', 'birth_date',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    op.alter_column('character', 'height',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('character', 'hair_color',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('character', 'eye_color',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('character', 'skin_color',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('character', 'url_image',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.alter_column('character', 'description',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.drop_index('description', table_name='character')
    op.drop_index('description_2', table_name='character')
    op.add_column('favorite', sa.Column('category_id', sa.Integer(), nullable=True))
    op.add_column('favorite', sa.Column('category_fk_id', sa.Integer(), nullable=True))
    op.drop_constraint('favorite_ibfk_1', 'favorite', type_='foreignkey')
    op.drop_constraint('favorite_ibfk_3', 'favorite', type_='foreignkey')
    op.drop_constraint('favorite_ibfk_2', 'favorite', type_='foreignkey')
    op.drop_constraint('favorite_ibfk_5', 'favorite', type_='foreignkey')
    op.create_foreign_key(None, 'favorite', 'category', ['category_id'], ['id'])
    op.drop_column('favorite', 'vehicle_id')
    op.drop_column('favorite', 'starship_id')
    op.drop_column('favorite', 'planet_id')
    op.drop_column('favorite', 'character_id')
    op.alter_column('planet', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('planet', 'population',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('planet', 'terrain',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('planet', 'climate',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('planet', 'orbit_period',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('planet', 'orbit_rotation',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('planet', 'diameter',
               existing_type=mysql.INTEGER(),
               nullable=True)
    op.alter_column('planet', 'url_image',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.alter_column('planet', 'description',
               existing_type=mysql.VARCHAR(length=200),
               nullable=True)
    op.drop_index('description', table_name='planet')
    op.drop_index('description_2', table_name='planet')
    op.alter_column('starship', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('user', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('user', 'last_name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=40),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    op.alter_column('user', 'creation_date',
               existing_type=mysql.VARCHAR(length=10),
               nullable=True)
    op.alter_column('vehicle', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=True)
    op.alter_column('vehicle', 'model',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.drop_index('description', table_name='vehicle')
    op.drop_index('description_2', table_name='vehicle')



def downgrade():

    op.create_index('description_2', 'vehicle', ['description'], unique=False)
    op.create_index('description', 'vehicle', ['description'], unique=False)
    op.alter_column('vehicle', 'model',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('vehicle', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.alter_column('user', 'creation_date',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=mysql.VARCHAR(length=40),
               nullable=False)
    op.alter_column('user', 'username',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('user', 'last_name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.alter_column('user', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.alter_column('starship', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.create_index('description_2', 'planet', ['description'], unique=False)
    op.create_index('description', 'planet', ['description'], unique=False)
    op.alter_column('planet', 'description',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.alter_column('planet', 'url_image',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.alter_column('planet', 'diameter',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('planet', 'orbit_rotation',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('planet', 'orbit_period',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('planet', 'climate',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('planet', 'terrain',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('planet', 'population',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('planet', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.add_column('favorite', sa.Column('character_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('favorite', sa.Column('planet_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('favorite', sa.Column('starship_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('favorite', sa.Column('vehicle_id', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'favorite', type_='foreignkey')
    op.create_foreign_key('favorite_ibfk_5', 'favorite', 'vehicle', ['vehicle_id'], ['id'])
    op.create_foreign_key('favorite_ibfk_2', 'favorite', 'planet', ['planet_id'], ['id'])
    op.create_foreign_key('favorite_ibfk_3', 'favorite', 'starship', ['starship_id'], ['id'])
    op.create_foreign_key('favorite_ibfk_1', 'favorite', 'character', ['character_id'], ['id'])
    op.drop_column('favorite', 'category_fk_id')
    op.drop_column('favorite', 'category_id')
    op.create_index('description_2', 'character', ['description'], unique=False)
    op.create_index('description', 'character', ['description'], unique=False)
    op.alter_column('character', 'description',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.alter_column('character', 'url_image',
               existing_type=mysql.VARCHAR(length=200),
               nullable=False)
    op.alter_column('character', 'skin_color',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('character', 'eye_color',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('character', 'hair_color',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('character', 'height',
               existing_type=mysql.INTEGER(),
               nullable=False)
    op.alter_column('character', 'birth_date',
               existing_type=mysql.VARCHAR(length=10),
               nullable=False)
    op.alter_column('character', 'gender',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    op.alter_column('character', 'name',
               existing_type=mysql.VARCHAR(length=30),
               nullable=False)
    op.drop_table('category')

