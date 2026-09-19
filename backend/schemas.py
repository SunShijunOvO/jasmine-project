"""定义接口输入校验、类型转换与响应序列化所需的数据结构。"""

# 标准库 Enum 用于定义有限且命名明确的投递进度集合。
from enum import Enum

# 标准库 date 让 Pydantic 把日期输入解析为真正的年月日对象。
from datetime import date

# Pydantic 工具分别用于建立数据模型、设置统一解析规则和声明字段约束。
from pydantic import BaseModel, ConfigDict, Field


# 投递进度的有限合法值，同时作为接口输入和 ORM 状态字段的共享类型。
class ApplicationStatus(str, Enum):
    APPLIED = "applied"
    AWAITING_WRITTEN = "awaiting_written"
    FINISHED_WRITTEN = "finish_written"
    AWAITING_INTERVIEW = "awaiting_interview"
    FINISHED_INTERVIEW = "finish_interview"
    OFFERED = "offered"
    REJECTED = "rejected"
    STOPPED = "stopped"


# 描述新增投递请求，并负责去除文本首尾空白、解析日期和校验状态。
class ApplicationCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    company_name: str = Field(min_length=1)
    position_name: str = Field(min_length=1)
    applied_on: date
    status: ApplicationStatus


# 描述返回给客户端的已保存记录，并允许从 ORM 对象属性读取数据库值。
class ApplicationRead(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True, from_attributes=True)
    id: int
    company_name: str = Field(min_length=1)
    position_name: str = Field(min_length=1)
    applied_on: date
    status: ApplicationStatus
