from typing import Any , Dict
from sqlalchemy.orm import Session
import requests
from fastapi import Request

from models import auto_project_api
from utils import tools_func
from models import auto_project_api
from api.v1.auto_project_api.crud.auto_project_api import curd_project_api
from api.v1.auto_project_config.crud.auto_project_config import crud_project_config
from common.assert_case import assert_case_class



class CURDAutoProjectCase():
    def __init__(self):
        self.model = auto_project_api.AutoProjectApiGroup
    def get_project_case(
            self , * , db : Session , project_api_id : int
    ) -> Dict:
        project_case_list = db.query(self.model).filter(self.model.project_api_id == project_api_id).all()
        data_response = tools_func.serialize_sqlalchemy_obj(project_case_list)
        return data_response
    def get_project_case_by_id(
            self , * , db : Session , project_case_id : int
    ) -> auto_project_api.AutoProjectApiGroup:
        project_case_obj = db.query(self.model).filter(self.model.id == project_case_id).first()
        return project_case_obj
    async def run_project_case(
            self , * ,db : Session ,request : Request, project_case_id : int , api_host : str , api_port : str
    ):
        project_case_obj = self.get_project_case_by_id(db = db , project_case_id = project_case_id)
        project_api_obj =  curd_project_api.get_project_api_by_id(db = db , project_api_id = project_case_obj.project_api_id)

        print('1')
        config_info = await crud_project_config.get_project_config(request = request , project_id = project_api_obj.project_id)
        print(config_info)
        print(type(config_info))
        url = tools_func.re_sub_url(project_api_obj.api_url , config = config_info)
        assert_case = project_case_obj.asert_case
        request_body = project_case_obj.request_body
        assert_result_list = []
        if project_api_obj.api_request_method == 'get':
            print(url)
            url = "http://" + api_host+":" + api_port + url
            if project_case_obj.request_body:
                response = requests.get(url=url,params = request_body)
            else:
                response = requests.get(url=url)
            assert_result_list.append(response.text)
            for item in assert_case:
                actual_value = assert_case_class.get_actual_vaule(response , item['assert_key'])
                if item['comparison_operator'] == 'equal':
                    assert_result = assert_case_class.equal_comparison(actual_value , item['assert_value'])
                    assert_result_list.append(assert_result)
                elif item['comparison_operator'] == 'not equal':
                    pass
        print(assert_result_list)
        return assert_result_list
crud_project_case = CURDAutoProjectCase()