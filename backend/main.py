"""创建 FastAPI 应用并定义当前可用的 HTTP 路由。"""

# FastAPI 创建 Web 应用，Depends 声明由框架提供的请求依赖。
from fastapi import FastAPI, Depends

# Schema 分别描述新增接口的请求输入和已保存记录的响应输出。
from backend.schemas import ApplicationCreate, ApplicationRead

# Session 类型描述路由参数获得的 ORM 工作单元，并提供 add、commit、refresh 等操作。
from sqlalchemy.orm import Session

# get_db 为每次请求创建 Session，并在请求结束后负责关闭。
from backend.database import get_db

# Application 是 applications 表的 ORM 映射，用于把已校验请求转换为待保存对象。
from backend.models import Application

# select 用于构造 ORM 查询语句；实际执行仍由请求级 Session 负责。
from sqlalchemy import select

app = FastAPI()


# 注册健康检查路由，用于确认应用能够正常响应请求。
@app.get("/health")
def health_check():
    return {"status": "ok"}


# 注册新增投递路由；保存后按 ApplicationRead 返回包含数据库主键的记录。
@app.post("/applications", response_model=ApplicationRead, status_code=201)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    # 将已经过接口校验的数据转换为 ORM 对象，主键稍后由数据库生成。
    db_application = Application(
        company_name=application.company_name,
        position_name=application.position_name,
        applied_on=application.applied_on,
        status=application.status,
    )
    # 将对象加入当前 Session 的待新增集合，此时尚未保证持久保存。
    db.add(db_application)
    # 提交当前事务；成功后新增记录才在请求结束后继续存在。
    db.commit()
    # 重新读取已提交记录，使数据库生成的主键等最新值加载回 ORM 对象。
    db.refresh(db_application)
    return db_application


# 注册投递集合读取路由；响应模型会逐项序列化查询得到的 ORM 对象。
@app.get("/applications", response_model=list[ApplicationRead])
def get_application(db: Session = Depends(get_db)):
    # 执行集合查询，并从结果行中提取 Application 对象形成响应列表。
    return db.execute(select(Application)).scalars().all()

