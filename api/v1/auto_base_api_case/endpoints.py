from fastapi import APIRouter,Depends , File
from sqlalchemy.orm import Session
from common import deps
from .schemas import auto_base_api_case_schemas
from typing import Any
from common import response_code
from .curd.auto_base_api_case import curd_base_case
# pip install python-multipart
import yaml
router = APIRouter()


@router.get('/getBaseCase')
def get_base_case(
        *,
        db : Session = Depends(dependency = deps.get_db),
        api_id : int = Depends(deps.get_base_api)
) -> Any :

    return response_code.resp_200(data = {
        "projectname": "test1",
        "projectuser": "test2"
    })
@router.post('/addBaseCase')
def add_base_case(
        *,
        db : Session = Depends(dependency = deps.get_db),
        api_id : int = Depends(dependency = deps.get_base_api),
        case_in : auto_base_api_case_schemas.BaseCaseCreate
) -> Any:
    curd_base_case.create_base_case(db = db , obj_in = case_in , base_api_id = api_id)
    return response_code.resp_200()

@router.post('/updateBaseCase')
def update_base_case(
        *,
        db : Session = Depends(dependency = deps.get_db),
        obj_in : auto_base_api_case_schemas.BaseCaseUpdate
) -> Any:
    curd_base_case.update_base_case(db = db , obj_in = obj_in)
    pass
@router.get('/deleteBaseCase')
def delete_base_case(
        *,
        db : Session = Depends(dependency = deps.get_db),
        id : int
) -> Any:
    curd_base_case.remove(db = db , id = id)
    pass
@router.post("/addBaseCaseMore")
def add_base_case_more(
        *,
        db : Session = Depends(dependency = deps.get_db),
        file: bytes = File(...)
):
    case_list = yaml.load(file , Loader=yaml.FullLoader)
    curd_base_case.create_base_case_more(db = db , obj_in = case_list)

    print(yaml.load(file))
    return file
