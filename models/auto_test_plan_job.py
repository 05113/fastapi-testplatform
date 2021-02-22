from sqlalchemy import Column,VARCHAR,Text,Integer,ForeignKey,JSON,Boolean
from sqlalchemy.orm import relationship


from db.base_class import Base

class AutoTestPlanJob(Base):
    __tablename__ = "auto_test_plan_job"
    state = Column(VARCHAR(100))
    success_count = Column(Integer)
    fail_count = Column(Integer)
    test_plan_id = Column(Integer,ForeignKey("auto_test_plan.id"))
    test_plan_result = Column(Boolean)
    to_test_plan = relationship("AutoTestPlan" , backref = "job2plan")

