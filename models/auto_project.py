from sqlalchemy import Boolean,Integer,Column,String,VARCHAR
from db.base_class import Base

class AutoProject(Base):
    __tablename__ = "auto_project"
    project_name = Column(VARCHAR(128),unique = True)
    project_user = Column(VARCHAR(128))
