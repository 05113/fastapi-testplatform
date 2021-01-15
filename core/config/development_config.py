from typing import Union,Optional

from pydantic import AnyHttpUrl,BaseSettings,IPvAnyAddress

class Settings(BaseSettings):
    Debug: bool = True
    Title: str = 'PlatForm'


    # mysql环境配置
    MYSQL_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    MYSQL_PORT: int = 3306
    MYSQL_USERNAME: str = "root"
    MYSQL_PASSWORD: str = "root123"
    MYSQL_DATABASE: str = "platform_test"

    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

settings = Settings()