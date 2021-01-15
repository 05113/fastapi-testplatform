from pydantic import BaseModel
from datetime import datetime
class BaseApiCreate(BaseModel):
    api_name : str = None
    api_url : str = None
    api_request_method : str = None
    api_content_type : str = None
class BaseApiUpdate(BaseApiCreate):
    id : int
class BaseApi(BaseApiUpdate):
    is_delete : int
    create_time : datetime
    update_time : datetime
    class Config:
        orm_mode = True