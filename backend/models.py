"""定义 Python ORM 对象与数据库表之间的映射。"""

# 标准库 date 表示只有年月日的投递日期，并作为 ORM 属性的 Python 类型。
from datetime import date
# SQLAlchemy Enum 配置状态列的数据库表示及 CHECK 约束。
from sqlalchemy import Enum
# Mapped 声明 ORM 属性类型，mapped_column 配置属性对应的数据库列。
from sqlalchemy.orm import Mapped, mapped_column
# 继承共享 Base，使本模型登记到同一份 metadata。
from backend.database import Base
# 复用接口层的有限状态集合，保持请求校验与数据库映射使用同一组业务状态。
from backend.schemas import ApplicationStatus

# 将 Application 对象映射到 applications 表；定义模型本身不会自动建表。
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
