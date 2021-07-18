from pydantic import BaseModel
from typing import List

class TestPlanCreate(BaseModel):
    test_plan_name : str
    test_plan_describe : str
    test_plan_host : str
    test_plan_port : int
    test_plan_api_group : List
class TestPlanUpdate(BaseModel):
    test_plan_name: str = None
    test_plan_describe: str = None
    test_plan_host: str = None
    test_plan_port: int = None
    test_plan_api_group: List = None