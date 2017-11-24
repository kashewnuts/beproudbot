"""initialize

Revision ID: 919388975e00
Revises: 
Create Date: 2017-10-30 10:01:12.176903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919388975e00'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cleaning',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slack_id', sa.Unicode(length=11), nullable=False),
    sa.Column('day_of_week', sa.Integer(), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('create_command',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=100), nullable=False),
    sa.Column('creator', sa.Unicode(length=100), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('kintai_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Unicode(length=100), nullable=False),
    sa.Column('is_workon', sa.Boolean(), nullable=True),
    sa.Column('registered_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('kudo_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Unicode(length=100), nullable=False),
    sa.Column('from_user_id', sa.Unicode(length=100), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('redbull_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Unicode(length=100), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('redmine_projectchannel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('channels', sa.Unicode(length=249), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('project_id')
    )
    op.create_table('redmine_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Unicode(length=9), nullable=False),
    sa.Column('api_key', sa.Unicode(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('api_key'),
    sa.UniqueConstraint('user_id')
    )
    op.create_table('thx_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Unicode(length=100), nullable=False),
    sa.Column('from_user_id', sa.Unicode(length=100), nullable=False),
    sa.Column('word', sa.Unicode(length=1024), nullable=False),
    sa.Column('channel_id', sa.Unicode(length=100), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_alias_name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slack_id', sa.Unicode(length=100), nullable=False),
    sa.Column('alias_name', sa.Unicode(length=100), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('alias_name')
    )
    op.create_table('water_history',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Unicode(length=100), nullable=False),
    sa.Column('delta', sa.Integer(), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('term',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('create_command', sa.Integer(), nullable=True),
    sa.Column('word', sa.Unicode(length=1024), nullable=False),
    sa.Column('creator', sa.Unicode(length=100), nullable=False),
    sa.Column('ctime', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['create_command'], ['create_command.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('word')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('term')
    op.drop_table('water_history')
    op.drop_table('user_alias_name')
    op.drop_table('thx_history')
    op.drop_table('redmine_users')
    op.drop_table('redmine_projectchannel')
    op.drop_table('redbull_history')
    op.drop_table('kudo_history')
    op.drop_table('kintai_history')
    op.drop_table('create_command')
    op.drop_table('cleaning')
    ### end Alembic commands ###