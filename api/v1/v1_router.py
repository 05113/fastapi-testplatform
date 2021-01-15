from fastapi import APIRouter , Depends
from .auto_project.endpoints import router as auto_project_router
from .auto_base_api.endpoints import router as auto_base_api_router

api_v1_router = APIRouter()
api_v1_router.include_router(auto_project_router , prefix = '/auto_project' , tags = ['项目'])
api_v1_router.include_router(auto_base_api_router , prefix = '/auto_base_api' , tags = ['基本api'] )