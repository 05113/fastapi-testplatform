from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from typing import Any

from common import deps
from .crud.auto_project_api import curd_project_api
from .schemas import auto_project_api_schemas

router = APIRouter()

@router.get('/addProjectApi' , summary = '添加项目api')
def add_project_api(
        *,
        db : Session = Depends(dependency = deps.get_db),
        project_id : int = Depends(dependency = deps.get_project),
        base_api_id : int = Depends(dependency = deps.get_base_api)
) -> Any:

    curd_project_api.addApi(db = db , project_id = project_id , base_api_id = base_api_id)
@router.post('updateProjectApi' , summary= '修改项目api')
def update_project_api(
        *,
        db : Session = Depends(dependency = deps.get_db),
        project_api_id : int = Depends(dependency = deps.get_project_api),
        obj_in : auto_project_api_schemas.updateProjectApi
)-> Any:
    curd_project_api.update_project_api(db = db , obj_in = obj_in , project_api_id = project_api_id)
@router.get('deleteProjectApi' , summary = '删除项目api')
def delete_project_api(
        *,
        db : Session = Depends(dependency = deps.get_db),
        project_api_id : int = Depends(dependency = deps.get_project_api)
) -> Any:
    curd_project_api.remove(db = db , id = project_api_id)

