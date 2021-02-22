from fastapi import Request
from typing import Any

from db.sys_redis import redis_client



class CRUDProjectConfig():
    def add_project_config(
            self , project_id , key , value
    ) -> Any:
        # await request.app.state.redis.hmset(project_id, key,value)
        dict = {}
        dict[key] = value
        redis_client.hmset(project_id, dict)
        pass
    def get_project_config(
            self , project_id
    ) -> Any:
        project_config = redis_client.hgetall(project_id)
        return project_config

crud_project_config = CRUDProjectConfig()