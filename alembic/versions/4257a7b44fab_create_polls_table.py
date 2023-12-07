"""create_polls_table

Revision ID: 4257a7b44fab
Revises: 0964df4ceba6
Create Date: 2023-12-03 23:21:17.132706

"""
import enum
from alembic import op
import sqlalchemy as sa

pg = sa.dialects.postgresql

class PollType(enum.Enum):
    text = 1
    image = 2


# revision identifiers, used by Alembic.
revision = '4257a7b44fab'
down_revision = '0964df4ceba6'
branch_labels = None
depends_on = None


def upgrade():
    # create_type=False
    op.create_table(
        'polls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String(255), nullable=False),
        sa.Column('type', sa.Enum(PollType, create_type=False), nullable=False),
        sa.Column('is_add_choices_active', sa.Boolean, nullable=False),
        sa.Column('is_voting_active', sa.Boolean, nullable=False),
        sa.Column('created_by', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
    )


def downgrade():
    op.drop_table('polls')