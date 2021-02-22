from fastapi import Depends , APIRouter ,Request
from sqlalchemy.orm import Session
from typing import Any

from common import deps
from .crud.auto_project_api_case import crud_project_case
from common import response_code

router = APIRouter()

@router.get('/')
async def test_redis(request : Request , num : int):
    await request.app.state.redis.hmset(1, num,'200')

@router.get('/getProjectCaseInfo')
def get_projectCaseInfo(
        *,
        db : Session = Depends(dependency = deps.get_db),
        project_api_id : int = Depends(dependency = deps.get_project_api)
) -> Any:
    response_data = crud_project_case.get_project_case(db = db , project_api_id = project_api_id)
    return response_code.resp_200(data = response_data)

@router.get('/runProjectCase')
def run_project_case(
        *,
        db : Session = Depends(dependency = deps.get_db),
        project_case_id : int = Depends(dependency = deps.get_project_case),
        api_host : str,
        api_port : str
) -> Any:
    result , list  = crud_project_case.run_project_case(
            db = db ,
            project_case_id = project_case_id ,
            api_host = api_host,
            api_port = api_port
        )

    return result

