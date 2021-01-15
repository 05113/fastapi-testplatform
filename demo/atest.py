from  sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean,Integer,Column,String
from core.config import  settings


# url = f"mysql+pymysql://root:root123@127.0.0.1:3306/platform_test?charset=utf8mb4"
url = settings.SQLALCHEMY_DATABASE_URL
engine = create_engine(url)
Base = declarative_base()

class News(Base):
    __tablename__ = "news"
    id = Column(Integer,primary_key=True)
    title = Column(String(200))

if __name__ == '__main__':
    News.metadata.create_all(engine)