from sqlalchemy import Boolean,Integer,Column,String,VARCHAR,ForeignKey,JSON
from sqlalchemy.orm import relationship
from db.base_class import Base

class AutoProjectApi(Base):
    __tablename__ = "auto_project_api"
    api_name = Column(VARCHAR(128),unique = True)
    api_url = Column(VARCHAR(128),unique = True)
    api_request_method = Column(VARCHAR(128))
    api_content_type = Column(JSON)
    project_id = Column(Integer,ForeignKey("auto_project.id"))
    to_auto_project = relationship("AutoProject" , backref = "api2project")
    is_enable = Column(Integer,default = 1,comment = "0=未启用,1=已启用")


class AutoProjectApiGroup(Base):
    __tablename__ = 'auto_project_api_group'
    case_name = Column(VARCHAR(128))
    request_body = Column(JSON)
    asert_case = Column(JSON)
    data_out = Column(VARCHAR(128))
    project_api_id = Column(Integer, ForeignKey("auto_project_api.id"))
    to_auto_project_api = relationship("AutoProjectApi" , backref = "group2api")

