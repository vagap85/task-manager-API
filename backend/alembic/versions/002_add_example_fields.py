"""Add example fields for demonstration

Revision ID: 002_add_example_fields
Revises: 001_initial
Create Date: 2025-12-18 01:40:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002_add_example_fields'
down_revision = '001_initial'
branch_labels = None
depends_on = None


def upgrade():
    # Пример добавления новых полей (закомментировано для демонстрации)
    # op.add_column('tasks', sa.Column('priority', sa.Integer(), server_default='1'))
    # op.add_column('tasks', sa.Column('due_date', sa.DateTime(), nullable=True))
    pass


def downgrade():
    # op.drop_column('tasks', 'due_date')
    # op.drop_column('tasks', 'priority')
    pass
