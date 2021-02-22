from sqlalchemy import Column,VARCHAR,Text,Integer,ForeignKey,JSON
from sqlalchemy.orm import relationship

from db.base_class import Base

class AutoTestPlan(Base):
    __tablename__ = "auto_test_plan"
    test_plan_name = Column(VARCHAR(100) , unique = True)
    test_plan_describe = Column(Text)
    test_plan_host = Column(VARCHAR(100))
    test_plan_port = Column(Integer)
    test_plan_api_group = Column(JSON)
    project_id = Column(Integer,ForeignKey("auto_project.id"))
    to_auto_project = relationship("AutoProject" , backref = "plan2project")

