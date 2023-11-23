"""Init

Revision ID: 626c883f726f
Revises: 
Create Date: 2023-09-28 20:17:47.330541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '626c883f726f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('cell_phone', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=120), nullable=False),
    sa.Column('last_name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('cell_phone', sa.String(length=100), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('start_work', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teachers_to_students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers_to_students')
    op.drop_table('teachers')
    op.drop_table('students')
    # ### end Alembic commands ###