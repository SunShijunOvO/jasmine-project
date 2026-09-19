"""建立数据库连接基础设施，并提供 Engine、Session 工厂与 ORM 共享 Base。"""

# SQLAlchemy 的 create_engine 根据数据库 URL 建立 Engine，作为连接池和数据库访问入口。
from sqlalchemy import create_engine
# ORM 工具分别提供模型共享基类和 Session 工厂，用于登记表结构及管理请求级数据库操作。
from sqlalchemy.orm import DeclarativeBase, sessionmaker
# 读取 config 模块已经校验的数据库参数，避免在此处硬编码连接信息。
from backend.config import settings
# URL 用结构化字段组装连接地址，正确处理密码等字段中的特殊字符。
from sqlalchemy.engine import URL

# 使用分项配置安全组装 SQLAlchemy 数据库 URL，避免手工拼接特殊字符。
db_url = URL.create(
    drivername="postgresql+psycopg",
    username=settings.user,
    password=settings.password.get_secret_value(),
    host=settings.host,
    port=settings.port,
    database=settings.name,
)

# Engine 是应用访问数据库的入口，并负责管理底层连接池。
engine = create_engine(db_url)

# SessionLocal 是绑定当前 Engine 的工厂；调用它才会创建独立 Session。
SessionLocal = sessionmaker(bind=engine)


# 为一次请求提供 Session，并在请求结束或发生异常后确保关闭。
def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


# 所有 ORM 模型继承同一个 Base，从而登记到共享 metadata。
class Base(DeclarativeBase):
    pass
