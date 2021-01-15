from fastapi import APIRouter , Depends
from typing import Any
from sqlalchemy.orm import Session
from common import deps , response_code
from .schemas.auto_base_api_schemas import *

from .crud.auto_base_api import curd_base_api
from utils.tools_func import serialize_sqlalchemy_obj


router = APIRouter()

@router.get('getBaseApi' , summary= '获取基础api信息')
async def getBaseApi(
            *,
            db : Session = Depends(dependency = deps.get_db),
) -> Any:
    # 获取分页数据模型
    BaseApiList = curd_base_api.get_multi(db = db)

    # 将数据模型序列化输出
    data_response = serialize_sqlalchemy_obj(BaseApiList)
    return response_code.resp_200(data = data_response)
@router.post('createBaseApi' , summary = '添加基础api信息')
async def addBaseApi(
        *,
        db : Session = Depends(dependency = deps.get_db),
        obj_in: BaseApiCreate
) -> Any:
    curd_base_api.create(db = db , obj_in = obj_in)
    return response_code.resp_200(data = {
        "projectname": "test1",
        "projectuser": "test2"
    })
@router.post('updateBaseApi' , summary = '修改基础api信息')
async def updateBaseApi(
        *,
        db : Session = Depends(dependency = deps.get_db),
        obj_in : BaseApiUpdate
) -> Any:
    curd_base_api.update(db = db , obj_in = obj_in)
    return response_code.resp_200(data = {
        "projectname": "test1",
        "projectuser": "test2"
    })
@router.get('deleteBaseApi' , summary = '删除基础api信息')
def deleteBaseApi(
        *,
        db : Session = Depends(dependency = deps.get_db),
        id : str
) -> Any:
    curd_base_api.remove(db = db , id = id)
    return response_code.resp_200(data = {
        "projectname": "test1",
        "projectuser": "test2"
    })
@router.get('enbaleBaseApi' , summary = '启用/禁用基础api信息')
def enableBaseApi(
        *,
        db : Session = Depends(dependency=deps.get_db),
        id : int,
        is_enable : int
) -> Any:
    curd_base_api.is_enable(db = db, id = id , is_enable = is_enable)
    return response_code.resp_200(data = {
        "projectname": "test1",
        "projectuser": "test2"
    })
