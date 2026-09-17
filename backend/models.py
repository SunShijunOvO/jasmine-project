from datetime import date
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column
from backend.database import Base
from backend.schemas import ApplicationStatus


class Application(Base):
    __tablename__ = "applications"
    id: Mapped[int] = mapped_column(primary_key=True)
    company_name: Mapped[str] = mapped_column(nullable=False)
    position_name: Mapped[str] = mapped_column(nullable=False)
    applied_on: Mapped[date] = mapped_column(nullable=False)
    status: Mapped[ApplicationStatus] = mapped_column(
        Enum(
            ApplicationStatus,
            native_enum=False,
            create_constraint=True,
            name="application_status",
        ),
        nullable=False,
    )
