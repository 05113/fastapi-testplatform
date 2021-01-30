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

    REDIS_HOST: Union[AnyHttpUrl, IPvAnyAddress] = "127.0.0.1"
    REDIS_PASSWORD : str = ''
    REDIS_PORT : int = 6379
    REDIS_DB : int = 0

    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"

    REDIS_URL: str = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}?encoding=utf-8"


settings = Settings()