from fastapi import APIRouter , Request ,Depends
from typing import Any
import json

from common import deps ,response_code
from .crud.auto_project_config import crud_project_config
from db.sys_redis import redis_client


router = APIRouter()

@router.post('/addProjectConfig' , summary = '添加项目配置信息')
def add_project_config(
        *,
        project_id : int = Depends(dependency = deps.get_project),
        key : str ,
        value : Any
) -> Any:

    crud_project_config.add_project_config(project_id = project_id , key = key , value = value)
    pass
@router.get('/getProjectConfig' , summary = '获取项目配置信息')
def get_project_config(
        *,
        project_id : int = Depends(dependency = deps.get_project)
) -> Any:
    # project_config = await crud_project_config.get_project_config(request = request,project_id = project_id)
    project_config = crud_project_config.get_project_config(project_id = project_id)

    print(project_config)
    return response_code.resp_200(data = project_config )
