from fastapi import APIRouter , Depends
from .auto_project.endpoints import router as auto_project_router
from .auto_base_api.endpoints import router as auto_base_api_router
from .auto_base_api_case.endpoints import router as auto_base_case_router
from .auto_project_api.endpoints import router as auto_project_api_router
from .auto_project_api_case.endpoints import router as auto_project_case_router
from .auto_project_config.endpoints import router as auto_project_config_router
from .auto_test_plan.endpoints import router as auto_test_plan_router

api_v1_router = APIRouter()
api_v1_router.include_router(auto_project_router , prefix = '/auto_project' , tags = ['项目'])
api_v1_router.include_router(auto_base_api_router , prefix = '/auto_base_api' , tags = ['基本api'] )
api_v1_router.include_router(auto_base_case_router , prefix = '/auto_base_case' , tags = ['基本case'])
api_v1_router.include_router(auto_project_api_router , prefix = '/auto_project_api' , tags = ['项目api'])
api_v1_router.include_router(auto_project_case_router , prefix='/auto_project_case' ,tags= ['项目case'])
api_v1_router.include_router(auto_project_config_router , prefix='/auto_project_config' , tags = ['项目配置'])
api_v1_router.include_router(auto_test_plan_router , prefix='/auto_test_plan' , tags = ['测试计划'])