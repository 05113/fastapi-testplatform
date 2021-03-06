from sqlalchemy import Boolean,Integer,Column,String,VARCHAR,ForeignKey,JSON
from sqlalchemy.orm import relationship
from db.base_class import Base

class AutoBaseApi(Base):
    __tablename__ = "auto_base_api"
    api_name = Column(VARCHAR(128),unique = True)
    api_url = Column(VARCHAR(128),unique = True)
    api_request_method = Column(VARCHAR(128))
    api_content_type = Column(JSON)
    is_enable = Column(Integer,default = 1,comment = "0=未启用,1=已启用")

class AutoBaseApiGroup(Base):
    __tablename__ = 'auto_base_api_group'
    case_name = Column(VARCHAR(128))
    request_body = Column(JSON)
    asert_case = Column(JSON)
    data_out = Column(VARCHAR(128))
    base_api_id = Column(Integer, ForeignKey("auto_base_api.id"))
    to_auto_base_api_ = relationship("AutoBaseApi" , backref = "group2api")

