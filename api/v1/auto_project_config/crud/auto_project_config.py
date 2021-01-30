from fastapi import Request
from typing import Any


class CRUDProjectConfig():
    async def add_project_config(
            self , request : Request , project_id , key , value
    ) -> Any:
        await request.app.state.redis.hmset(project_id, key,value)
        pass
    async def get_project_config(
            self , request : Request , project_id
    ) -> Any:
        project_config = await request.app.state.redis.hgetall(project_id)
        return project_config

crud_project_config = CRUDProjectConfig()