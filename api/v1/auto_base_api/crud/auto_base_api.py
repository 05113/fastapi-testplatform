from common.curd_base import CRUDBase
from models.auto_base_api import AutoBaseApi
from ..schemas import  auto_base_api_schemas
from sqlalchemy.orm import Session
from typing import Any

class CRUDAutoBaseApi(CRUDBase[AutoBaseApi , auto_base_api_schemas.BaseApiCreate , auto_base_api_schemas.BaseApiUpdate]):
    def create(self, db: Session, *, obj_in: auto_base_api_schemas.BaseApiCreate) -> AutoBaseApi:
        obj_in = AutoBaseApi(
            api_name = obj_in.api_name,
            api_url = obj_in.api_url,
            api_request_method = obj_in.api_request_method,
            api_content_type = obj_in.api_content_type
        )
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def update(self,db : Session , * , obj_in : auto_base_api_schemas.BaseApiUpdate) -> Any:
        obj_in = AutoBaseApi(
            id = obj_in.id,
            api_name = obj_in.api_name,
            api_url = obj_in.api_url,
            api_request_method = obj_in.api_request_method,
            api_content_type = obj_in.api_content_type,
        )
        if obj_in.api_name is not None:
            obj = db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.api_name : obj_in.api_name})
        if obj_in.api_url is not None:
            obj = db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.api_url : obj_in.api_url})
        if obj_in.api_request_method is not None:
            obj = db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.api_request_method : obj_in.api_request_method})
        if obj_in.api_content_type is not None:
            obj = db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.api_content_type : obj_in.api_content_type})
        db.commit()
        return obj
    def is_enable(self, * ,db : Session , is_enable : int , id : int):
        db = db
        obj = db.query(self.model).filter(self.model.id == id).update({self.model.is_enable : is_enable})
        db.commit()
        return obj
curd_base_api = CRUDAutoBaseApi(AutoBaseApi)