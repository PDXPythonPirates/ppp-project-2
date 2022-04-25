"""users table

Revision ID: 82cb157dce31
Revises: 
Create Date: 2022-04-05 02:11:54.250824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "82cb157dce31"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("username", sa.String(length=32), nullable=False),
        sa.Column("email", sa.String(length=64), nullable=True),
        sa.Column("password_hash", sa.String(length=128), nullable=True),
        sa.PrimaryKeyConstraint("username"),
    )
    op.create_index(op.f("ix_user_email"), "user", ["email"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_user_email"), table_name="user")
    op.drop_table("user")
    # ### end Alembic commands ###
