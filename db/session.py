from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

url = settings.SQLALCHEMY_DATABASE_URL

engine = create_engine(url, pool_pre_ping=True)

DbSession = sessionmaker(bind=engine,autocommit=False, autoflush=False,)
# 操作数据库
# session = DbSession()
