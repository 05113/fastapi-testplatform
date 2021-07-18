from fastapi import APIRouter
from typing import Dict

from .crud.auto_tools_api import crud_tools_api
from common.response_code import *
router = APIRouter()


@router.post('/sleep_fun')
def sleep_fun(sleeptime : dict):
    '''
    sleeptime:{"sleeptime":2}
    '''
    crud_tools_api.sleep_fun(sleeptime)
    return resp_200()



@router.post('sql_fun')

def sql_fun(* ,
            sql_info : Dict,
):
    '''
    sql_info:{
    "username":"root",
    "password":"root123",
    "host":"127.0.0.1",
    "port":3306,
    "database":"platform_test",
    "sql":"select * from auto_base_api"
    }
    '''
    data_response = crud_tools_api.sql_fun(sql_info = sql_info)
    return resp_200(data = data_response)
