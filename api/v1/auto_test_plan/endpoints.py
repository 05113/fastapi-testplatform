from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session

from common import deps
from .schemas.auto_test_plan_schemas import *
from .crud.auto_test_plan import crud_test_plan

router = APIRouter()

@router.post('/add_test_plan' ,summary = '创建测试计划')
def add_test_plan(
        *,
        db : Session = Depends(dependency = deps.get_db),
        project_id : int = Depends(dependency = deps.get_project),
        obj_in : TestPlanCreate
):
    crud_test_plan.add_test_plan(db = db , project_id = project_id , obj_in = obj_in)
    pass
@router.post('/update_test_plan')
def update_test_plan(
        *,
        db : Session = Depends(dependency = deps.get_db),
        test_plan_id : int = Depends(dependency = deps.get_test_plan),
        obj_in : TestPlanUpdate
):
    pass

@router.get('/run_test_plan')
def run_test_plan(
        *,
        db : Session = Depends(dependency = deps.get_db),
        test_plan_id : int = Depends(dependency = deps.get_test_plan)
):
    crud_test_plan.run_test_plan(db = db , test_plan_id = test_plan_id)

    return 1
