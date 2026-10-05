"""initial backend MVP schema"""
from alembic import op
from sqlalchemy import inspect

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    bind = op.get_bind()
    from app.models.base import Base
    from app.models import entities  # noqa: F401
    Base.metadata.create_all(bind=bind)

def downgrade():
    bind = op.get_bind()
    from app.models.base import Base
    from app.models import entities  # noqa: F401
    Base.metadata.drop_all(bind=bind)

