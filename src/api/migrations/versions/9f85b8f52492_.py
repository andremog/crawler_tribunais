"""empty message

Revision ID: 9f85b8f52492
Revises: 
Create Date: 2019-07-20 09:18:49.353276

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9f85b8f52492'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('process',
    sa.Column('number', sa.String(length=25), nullable=False),
    sa.Column('grade1', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('grade2', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('number')
    )
    op.create_table('rawHTML',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('number', sa.String(length=25), nullable=True),
    sa.Column('grade', sa.Integer(), nullable=True),
    sa.Column('_html', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rawHTML')
    op.drop_table('process')
    # ### end Alembic commands ###
