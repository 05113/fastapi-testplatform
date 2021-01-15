from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column,Integer,DateTime
from sqlalchemy.sql import func
from datetime import datetime

@as_declarative()
class Base:
    # index:是否是索引
    # autoincrement:主键自增
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    create_time = Column(DateTime, default=datetime.now, server_default=func.now(), comment="创建时间")
    update_time = Column(DateTime, default=datetime.now, onupdate=datetime.now, server_default=func.now(),
                         server_onupdate=func.now(), comment="更新时间")
    is_delete = Column(Integer, default=0, comment="逻辑删除:0=未删除,1=删除", server_default='0')

    __name__:str
    @declared_attr
    def __tablename__(cls) ->str:
        return cls.__name__.lower()
