from pydantic import BaseModel

class updateProjectApi(BaseModel):
    api_name : str = None
    api_url : str = None
    api_request_method : str = None
    api_content_type : str = None