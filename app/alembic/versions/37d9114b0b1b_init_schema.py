from collections.abc import Sequence

import sqlalchemy as sa
import sqlmodel
import sqlmodel.sql.sqltypes
from alembic import op

"""init schema

Revision ID: 37d9114b0b1b
Revises:
Create Date: 2024-11-19 18:32:14.986152

"""

# revision identifiers, used by Alembic.
revision: str = "37d9114b0b1b"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "mission",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "team",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("headquarters", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_team_name"), "team", ["name"], unique=False)
    op.create_table(
        "hero",
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("secret_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("team_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["team_id"],
            ["team.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "heromissionlink",
        sa.Column("hero_id", sa.Integer(), nullable=False),
        sa.Column("mission_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["hero_id"],
            ["hero.id"],
        ),
        sa.ForeignKeyConstraint(
            ["mission_id"],
            ["mission.id"],
        ),
        sa.PrimaryKeyConstraint("hero_id", "mission_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("heromissionlink")
    op.drop_table("hero")
    op.drop_index(op.f("ix_team_name"), table_name="team")
    op.drop_table("team")
    op.drop_table("mission")
    # ### end Alembic commands ###