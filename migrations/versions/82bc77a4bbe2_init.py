"""init

Revision ID: 82bc77a4bbe2
Revises: None
Create Date: 2014-12-25 23:48:38.426147

"""

# revision identifiers, used by Alembic.
revision = '82bc77a4bbe2'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('postid', sa.String(length=32), nullable=False),
        sa.Column('name', sa.String(length=128), nullable=False),
        sa.Column('tagline', sa.String(), nullable=False),
        sa.Column('date', sa.DateTime(), nullable=False),
        sa.Column('redirect_url', sa.String(length=256), nullable=False),
        sa.Column('discussion_url', sa.String(length=256), nullable=False),
        sa.Column('screenshot_url', sa.String(length=256), nullable=False),
        sa.Column('votes_count', sa.Integer(), nullable=True, default=0),
        sa.Column('comments_count', sa.Integer(), nullable=True, default=0),
        sa.Column('ctagline', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('postid')
    )

    op.create_table('groups',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('admin', sa.Boolean(), nullable=False),
        sa.Column('mod', sa.Boolean(), nullable=False),
        sa.Column('guest', sa.Boolean(), nullable=False),
        sa.Column('editproduct', sa.Boolean(), nullable=False),
        sa.Column('deleteproduct', sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )

    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(length=200), nullable=False),
        sa.Column('email', sa.String(length=200), nullable=False),
        sa.Column('password', sa.String(length=80), nullable=False),
        sa.Column('date_joined', sa.DateTime(), nullable=True),
        sa.Column('lastseen', sa.DateTime(), nullable=True),
        sa.Column('birthday', sa.DateTime(), nullable=True),
        sa.Column('gender', sa.String(length=10), nullable=True),
        sa.Column('website', sa.String(length=200), nullable=True),
        sa.Column('location', sa.String(length=100), nullable=True),
        sa.Column('signature', sa.Text(), nullable=True),
        sa.Column('avatar', sa.String(length=200), nullable=True),
        sa.Column('notes', sa.Text(), nullable=True),
        sa.Column('theme', sa.String(length=15), nullable=True),
        sa.Column('primary_group_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['primary_group_id'], ['groups.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )

    op.create_table('groups_users',
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('group_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('users')
    op.drop_table('groups')
    op.drop_table('groups_users')
    ### end Alembic commands ###
