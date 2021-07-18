from typing import Any , Dict , List
from sqlalchemy.orm import Session
import requests
from fastapi import Request
import traceback

from utils import tools_func
from models import auto_project_api
from api.v1.auto_project_api.crud.auto_project_api import curd_project_api
from api.v1.auto_project_config.crud.auto_project_config import crud_project_config
from common.assert_case import assert_case_class
from common.exc import MyException



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


    def run_project_case(
            self , * ,db : Session , project_case_id : int , api_host : str , api_port : str
    ) -> List:
        try:
            project_case_obj = self.get_project_case_by_id(db = db , project_case_id = project_case_id)
            project_api_obj =  curd_project_api.get_project_api_by_id(db = db , project_api_id = project_case_obj.project_api_id)

            config_info = crud_project_config.get_project_config(project_id = project_api_obj.project_id)
            print(config_info)
            print(type(config_info))
            url = tools_func.re_sub_url(project_api_obj.api_url , config = config_info)
            assert_case = project_case_obj.asert_case
            request_body = project_case_obj.request_body

            for item in request_body.keys():
                json_value = request_body[item]
                if isinstance(json_value , str):
                    if '$' in json_value:
                        re_value = self._get_request_body(db = db , request_body_value = json_value , project_case_id = project_case_obj.id)
                        request_body[item] = re_value

            assert_result_list = []
            if project_api_obj.api_request_method == 'get':
                print(url)
                url = "http://" + api_host+":" + api_port + url
                if project_case_obj.request_body:
                    response = requests.get(url=url,params = request_body)
                else:
                    response = requests.get(url=url)
                assert_result_list.append(response.text)
                assert_result = True
                for item in assert_case:
                    actual_value = assert_case_class.get_actual_vaule(response , item['assert_key'])
                    if item['comparison_operator'] == 'equal':
                        new_assert_result = assert_case_class.equal_comparison(actual_value , item['assert_value'])
                    elif item['comparison_operator'] == 'not equal':
                        pass
                    assert_result = assert_result and new_assert_result
                    assert_result_list.append(new_assert_result)
            print(assert_result_list)

            # todo ''空字符串进行判断
            if project_case_obj.data_out is not None:
                data_out = project_case_obj.data_out
                data_out_arr = data_out.split(';')
                for item in data_out_arr:
                    self._save_data_out(db = db , data_out_item = item , response = response , project_case_id = project_case_id)
            return assert_result,assert_result_list
        except MyException as e:
            message = e.__str__()


    def _save_data_out(self,db : Session, data_out_item : str , response , project_case_id : int):

        data_out_item_arr = data_out_item.split('=')
        data_out_left = data_out_item_arr[0]

        data_out_item_right = data_out_item_arr[1]

        data_out_key = data_out_left

        data_out_value = assert_case_class.get_actual_vaule(response = response , assert_key = data_out_item_right)

        # if '[' in data_out_item_right:
        #     data_out_item_right_arr = data_out_item_right.split('[')
        # else:
        #     data_out_value = response[data_out_item_right]

        case_obj = curd_project_api.get_project_id_by_case_id(db = db ,
                                                   case_id = project_case_id)
        
        crud_project_config.add_project_config(project_id = case_obj.project_id ,
                                               key = data_out_key,
                                               value = data_out_value)

    def _get_request_body(self , db : Session , request_body_value : str , project_case_id : int  ):
        case_obj = curd_project_api.get_project_id_by_case_id(db = db ,
                                                   case_id = project_case_id)

        config_dict = crud_project_config.get_project_config(case_obj.project_id)

        re_value = tools_func.re_get_request_body_value(request_body_value)

        return config_dict[re_value]

crud_project_case = CURDAutoProjectCase()