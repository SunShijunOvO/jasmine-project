"""读取并校验数据库连接配置，向应用提供统一的设置对象。"""

# pydantic-settings 负责从环境变量和 .env 读取配置；这里用它定义配置模型及读取规则。
from pydantic_settings import BaseSettings, SettingsConfigDict
# Pydantic 的 SecretStr 会遮蔽密码的常规显示，避免日志或调试输出直接暴露明文；它不负责加密。
from pydantic import SecretStr

# 从环境变量和本地 .env 文件读取数据库参数，并按字段类型进行校验。
class Settings(BaseSettings):
    host: str
    port: int
    name: str
    user: str
    password: SecretStr

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="DB_",
        extra="ignore",
    )

settings = Settings()
