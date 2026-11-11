
import uuid
from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, String, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        primary_key=True,
        default=uuid.uuid4,
    )

    actor_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("users.id"),
        nullable=False,
    )

    source_post_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("posts.id"),
        nullable=False,
    )

    target_post_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("posts.id"),
        nullable=False,
    )    

    type: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    ) 

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
