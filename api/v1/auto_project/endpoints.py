from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from common import deps , response_code
from typing import Any
from .schemas.auto_project_schemas import *
from models.auto_project import AutoProject
from .crud.auto_project import curd_project
import json
from utils.tools_func import serialize_sqlalchemy_obj


router = APIRouter()



@router.get('/getProject', summary = '获取项目信息')
async def get_project_info(*,
                           db:Session = Depends(deps.get_db),
) -> AutoProject:

    # 获取分页数据模型
    auto_project_list = curd_project.get_multi(db = db)
    # 将数据模型序列化输出
    data_response = serialize_sqlalchemy_obj(auto_project_list)

    return response_code.resp_200(data = data_response)

@router.post('/addProject', summary='添加项目')
async def create_project(
        *,
        db: Session = Depends(deps.get_db),
        obj_in: ProjectCreate
) -> AutoProject:
    # db_obj = AutoProject(
    #     project_name= obj_in.project_name,
    #     project_user= obj_in.project_user
    # )
    curd_project.create(db ,obj_in = obj_in )

    return response_code.resp_200(data = {
        "projectname": "test1",
        "projectuser": "test2"
    })
@router.post('/updateProject' , summary = '修改项目信息')
async def update_project(
        *,
        db : Session = Depends(deps.get_db),
        obj_in : ProjectUpdate
) -> AutoProject:
    curd_project.update(db = db , obj_in = obj_in)
    return response_code.resp_200(data={
        "projectname": "test1",
        "projectuser": "test2"
    })
@router.get('/deleteProject' , summary = '删除项目')
async def deleteProject(
        *,
        db : Session = Depends(deps.get_db),
        id : str
) -> Any:
    print(id)
    curd_project.remove(db = db , id = id)
    return response_code.resp_200(data={
        "projectname": "test1",
        "projectuser": "test2"
    })





