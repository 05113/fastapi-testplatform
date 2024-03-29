"""test plan1

Revision ID: fe8ae9435b50
Revises: 
Create Date: 2021-02-01 17:33:56.370358

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe8ae9435b50'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auto_base_api',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), server_default='0', nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('api_name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('api_url', sa.VARCHAR(length=128), nullable=True),
    sa.Column('api_request_method', sa.VARCHAR(length=128), nullable=True),
    sa.Column('api_content_type', sa.JSON(), nullable=True),
    sa.Column('is_enable', sa.Integer(), nullable=True, comment='0=未启用,1=已启用'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('api_name'),
    sa.UniqueConstraint('api_url')
    )
    op.create_index(op.f('ix_auto_base_api_id'), 'auto_base_api', ['id'], unique=False)
    op.create_table('auto_project',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), server_default='0', nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('project_name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('project_user', sa.VARCHAR(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('project_name')
    )
    op.create_index(op.f('ix_auto_project_id'), 'auto_project', ['id'], unique=False)
    op.create_table('auto_base_api_group',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), server_default='0', nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('case_name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('request_body', sa.JSON(), nullable=True),
    sa.Column('asert_case', sa.JSON(), nullable=True),
    sa.Column('data_out', sa.VARCHAR(length=128), nullable=True),
    sa.Column('base_api_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['base_api_id'], ['auto_base_api.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_auto_base_api_group_id'), 'auto_base_api_group', ['id'], unique=False)
    op.create_table('auto_project_api',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), server_default='0', nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('api_name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('api_url', sa.VARCHAR(length=128), nullable=True),
    sa.Column('api_request_method', sa.VARCHAR(length=128), nullable=True),
    sa.Column('api_content_type', sa.JSON(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('is_enable', sa.Integer(), nullable=True, comment='0=未启用,1=已启用'),
    sa.ForeignKeyConstraint(['project_id'], ['auto_project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('api_name'),
    sa.UniqueConstraint('api_url')
    )
    op.create_index(op.f('ix_auto_project_api_id'), 'auto_project_api', ['id'], unique=False)
    op.create_table('auto_test_plan',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), server_default='0', nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('test_plan_name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('test_plan_describe', sa.Text(), nullable=True),
    sa.Column('test_plan_host', sa.VARCHAR(length=100), nullable=True),
    sa.Column('test_plan_port', sa.Integer(), nullable=True),
    sa.Column('test_plan_api_group', sa.Text(), nullable=True),
    sa.Column('test_plan_state', sa.VARCHAR(length=100), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['auto_project.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('test_plan_name')
    )
    op.create_index(op.f('ix_auto_test_plan_id'), 'auto_test_plan', ['id'], unique=False)
    op.create_table('auto_project_api_group',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('create_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), server_default=sa.text('now()'), nullable=True, comment='更新时间'),
    sa.Column('is_delete', sa.Integer(), server_default='0', nullable=True, comment='逻辑删除:0=未删除,1=删除'),
    sa.Column('case_name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('request_body', sa.JSON(), nullable=True),
    sa.Column('asert_case', sa.JSON(), nullable=True),
    sa.Column('data_out', sa.VARCHAR(length=128), nullable=True),
    sa.Column('project_api_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_api_id'], ['auto_project_api.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_auto_project_api_group_id'), 'auto_project_api_group', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auto_project_api_group_id'), table_name='auto_project_api_group')
    op.drop_table('auto_project_api_group')
    op.drop_index(op.f('ix_auto_test_plan_id'), table_name='auto_test_plan')
    op.drop_table('auto_test_plan')
    op.drop_index(op.f('ix_auto_project_api_id'), table_name='auto_project_api')
    op.drop_table('auto_project_api')
    op.drop_index(op.f('ix_auto_base_api_group_id'), table_name='auto_base_api_group')
    op.drop_table('auto_base_api_group')
    op.drop_index(op.f('ix_auto_project_id'), table_name='auto_project')
    op.drop_table('auto_project')
    op.drop_index(op.f('ix_auto_base_api_id'), table_name='auto_base_api')
    op.drop_table('auto_base_api')
    # ### end Alembic commands ###
