from typing import Optional
from datetime import datetime


from pydantic import BaseModel


class ProjectNameBase(BaseModel):
    project_name: str


class ProjectUser(ProjectNameBase):
    project_user: str

class ProjectCreate(ProjectUser):
    pass
class ProjectUpdate(ProjectNameBase):
    id : int
class ProjectId(BaseModel):
    id : int
class Project(ProjectNameBase):
    id:int
    is_delete:int
    create_time:datetime
    update_time:datetime
    class Config:
        orm_mode = True
