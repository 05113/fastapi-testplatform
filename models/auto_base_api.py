from sqlalchemy import Boolean,Integer,Column,String,VARCHAR,ForeignKey
from sqlalchemy.orm import relationship
from db.base_class import Base

class AutoBaseApi(Base):
    __tablename__ = "auto_base_api"
    api_name = Column(VARCHAR(128),unique = True)
    api_url = Column(VARCHAR(128),unique = True)
    api_request_method = Column(VARCHAR(128))
    api_content_type = Column(VARCHAR(128))
    api_case_group_id = Column(Integer, ForeignKey("auto_base_api_group.id") , server_default='')
    is_enable = Column(Integer,default = 1,comment = "0=未启用,1=已启用")
    to_auto_base_api_group = relationship("AutoBaseApiGroup" , backref = "api2group")

class AutoBaseApiGroup(Base):
    __tablename__ = 'auto_base_api_group'
    case_name = Column(VARCHAR(128))
    request_body = Column(VARCHAR(128))
    asert_case = Column(VARCHAR(128))
    data_out = Column(VARCHAR(128))