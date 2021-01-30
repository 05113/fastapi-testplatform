from typing import Any
from sqlalchemy.orm import Session

from common.curd_base import CRUDBase
from models.auto_project_api import AutoProjectApi , AutoProjectApiGroup
from api.v1.auto_base_api.crud.auto_base_api import curd_base_api
from api.v1.auto_base_api_case.curd.auto_base_api_case import curd_base_case
from ..schemas import auto_project_api_schemas

class CURDAutoProjectApi(CRUDBase[AutoProjectApi,AutoProjectApi,AutoProjectApi]):
    def addApi(
            self , db : Session , project_id : int , base_api_id : int
    ) -> Any:
        base_api = curd_base_api.getInfoById(db = db , id = base_api_id)
        project_api_object = AutoProjectApi(api_name = base_api.api_name,
                                            api_url = base_api.api_url,
                                            api_request_method = base_api.api_request_method,
                                            api_content_type = base_api.api_content_type,
                                            is_enable = base_api.is_enable,
                                            project_id = project_id)
        db.add(project_api_object)
        db.flush()
        project_api_id = project_api_object.id

        case_list = curd_base_case.get_case_by_apiId(db = db , api_id = base_api_id)

        objects = [ AutoProjectApiGroup(case_name = obj.case_name,
                                        request_body = obj.request_body,
                                        asert_case = obj.asert_case,
                                        data_out = obj.data_out,
                                        project_api_id = project_api_id
                                        ) for obj in case_list]
        db.add_all(objects)
        db.commit()
    def get_project_api_by_id(
            self , * , db : Session , project_api_id : int
    ) -> AutoProjectApi:

        auto_project_api = db.query(self.model).filter(self.model.id == project_api_id).first()
        return auto_project_api
    def update_project_api(
            self , * ,db : Session , obj_in : auto_project_api_schemas.updateProjectApi , project_api_id : int
    ) -> Any:
        try:
            if obj_in.api_name is not None:
                db.query(self.model).filter(self.model.id == project_api_id).update({self.model.api_name : obj_in.api_name})
            if obj_in.api_url is not None:
                db.query(self.model).filter(self.model.id == project_api_id).update({self.model.api_url : obj_in.api_url})
            if obj_in.api_request_method is not None:
                db.query(self.model).filter(self.model.id == project_api_id).update({self.model.api_request_method : obj_in.api_request_method})
            if obj_in.api_content_type is not None:
                db.query(self.model).filter(self.model.id == project_api_id).update({self.model.api_content_type : obj_in.api_content_type})
            db.commit()
        except:
            db.rollback()
curd_project_api = CURDAutoProjectApi(AutoProjectApi)