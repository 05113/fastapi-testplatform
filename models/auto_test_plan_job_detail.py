from sqlalchemy import Column,VARCHAR,Text,Integer,ForeignKey,JSON
from sqlalchemy.orm import relationship


from db.base_class import Base

class AutoTestPlanJobDetail(Base):
    __tablename__ = "auto_test_plan_job_detail"
    api_id = Column(Integer)
    api_group_id = Column(Integer)
    response_body = Column(Text)
    api_group_result = Column(VARCHAR(100))
    test_plan_job_id = Column(Integer,ForeignKey("auto_test_plan_job.id"))
    to_test_plan_job = relationship("AutoTestPlanJob" , backref = "detail2job")