"""add colum update_at in  users table

Revision ID: dcbc3ffd8af5
Revises: e59fec4fc70c
Create Date: 2024-07-24 21:18:35.797025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dcbc3ffd8af5'
down_revision: Union[str, None] = 'e59fec4fc70c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###