"""language column added to Post table

Revision ID: 844e145e21b7
Revises: 20c9c75d600a
Create Date: 2019-02-02 17:53:28.188708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '844e145e21b7'
down_revision = '20c9c75d600a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
