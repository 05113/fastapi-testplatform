from typing import Generator, Any, Union, Optional
from db.session import DbSession
from sqlalchemy.orm import Session
from fastapi import Depends , HTTPException

from models import auto_base_api , auto_project_api
from api.v1.auto_base_api.crud.auto_base_api import curd_base_api
from api.v1.auto_project.crud.auto_project import curd_project
from api.v1.auto_project_api.crud.auto_project_api import curd_project_api
from api.v1.auto_project_api_case.crud.auto_project_api_case import crud_project_case
def get_db() -> Generator:
    try:
        db = DbSession()
        yield db
    finally:
        db.close()

def get_base_api(
        *,
        db : Session = Depends(dependency = get_db),
        base_api_id : int
) -> auto_base_api.AutoBaseApi :
    base_api = curd_base_api.getInfoById(db = db , id = base_api_id)
    if not base_api:
        raise HTTPException(status_code=404, detail="base_api not found")
    return base_api.id


def get_project(
        *,
        db : Session = Depends(dependency = get_db),
        project_id : int
) -> auto_base_api.AutoBaseApi :
    project_obj = curd_project.get_project_by_id(db = db , project_id = project_id)
    if not project_obj:
        raise HTTPException(status_code=404, detail="project not found")
    return project_obj.id


def get_project_api(
        *,
        db : Session = Depends(dependency = get_db),
        project_api_id : int
) -> auto_project_api.AutoProjectApi :
    project_api_obj = curd_project_api.get_project_api_by_id(db = db , project_api_id = project_api_id)
    if not project_api_obj:
        raise HTTPException(status_code=404, detail="project api not found")
    return project_api_obj.id

def get_project_case(
        *,
        db : Session = Depends(dependency = get_db),
        project_case_id : int
) -> auto_project_api.AutoProjectApiGroup :
    project_case_obj = crud_project_case.get_project_case_by_id(db = db , project_case_id = project_case_id)
    if not project_case_obj:
        raise HTTPException(status_code=404, detail="project case not found")
    return project_case_obj.id