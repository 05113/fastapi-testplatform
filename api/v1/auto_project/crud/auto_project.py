from common.curd_base import CRUDBase
from models.auto_project import AutoProject
from ..schemas import auto_project_schemas
from sqlalchemy.orm import Session
from common.exc import UnicornException
from common import response_code



class CRUDProject(CRUDBase[AutoProject , auto_project_schemas.ProjectCreate,auto_project_schemas.ProjectUpdate]):
    def create(self, db: Session, *, obj_in: auto_project_schemas.ProjectCreate) -> AutoProject:
        obj_in = AutoProject(
            project_name = obj_in.project_name,
            project_user = obj_in.project_user
        )
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def update(self, db : Session , * , obj_in : auto_project_schemas.ProjectUpdate) -> AutoProject:

        obj = db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.project_name: obj_in.project_name})
        db.commit()
        return obj
    def get_project_by_id(
            self , * , db : Session , project_id : int
    ) -> AutoProject:
        project_obj = db.query(self.model).filter(self.model.id == project_id).first()
        return project_obj
curd_project = CRUDProject(AutoProject)