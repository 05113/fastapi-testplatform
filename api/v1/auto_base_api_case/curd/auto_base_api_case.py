from common.curd_base import CRUDBase
from models.auto_base_api import AutoBaseApiGroup
from sqlalchemy.orm import Session
from ..schemas import auto_base_api_case_schemas
from common import deps
from typing import Any , List
import traceback
from fastapi import FastAPI
class CRUDAutoBaseCase(CRUDBase[AutoBaseApiGroup,AutoBaseApiGroup,AutoBaseApiGroup]):
    # [
    #     {"assert_key": "response.success",
    #      "comparison_operator": "equal",
    #      "assert_value": true
    #      }
    # ]
    def create_base_case(
        self , * , db : Session , obj_in : auto_base_api_case_schemas.BaseCaseCreate , base_api_id : int
    ) -> Any:
        obj_in = AutoBaseApiGroup(
            case_name = obj_in.case_name,
            request_body = obj_in.request_body,
            asert_case = obj_in.assert_case,
            data_out = obj_in.data_out,
            base_api_id = base_api_id
        )
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in
    def update_base_case(
            self , * , db : Session , obj_in : auto_base_api_case_schemas.BaseCaseUpdate
    ) -> Any:
        if obj_in.case_name is not None:
            db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.case_name : obj_in.case_name})
        if obj_in.request_body is not None:
            db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.request_body : obj_in.request_body})
        if obj_in.assert_case is not None:
            db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.asert_case : obj_in.assert_case})
        if obj_in.data_out is not None:
            db.query(self.model).filter(self.model.id == obj_in.id).update({self.model.data_out : obj_in.data_out})
        db.commit()
        return 1
    def create_base_case_more(
            self , * , db : Session , obj_in : List
    ) -> Any:
        try:
            for objs in obj_in:
                base_api_id = deps.get_base_api(db = db , base_api_id = objs['api_id'])
                objects = [AutoBaseApiGroup(case_name=obj['case_name'],
                                            request_body = obj['request_body'],
                                            asert_case = obj['asert_case'],
                                            data_out = obj['data_out'],
                                            base_api_id = base_api_id)
                           for obj in objs['caseCon']]
                db.add_all(objects)
            db.commit()
            print(objects)
        except:
            print(str(traceback.format_exc()))
            db.rollback()
        pass
    def get_case_by_apiId(
            self , * , db : Session , api_id : int
    ) -> Any:
        case_list = db.query(self.model).filter(self.model.base_api_id == api_id).all()
        return case_list
curd_base_case = CRUDAutoBaseCase(AutoBaseApiGroup)

