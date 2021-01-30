from pydantic import BaseModel
from typing import Dict ,List

class BaseCaseCreate(BaseModel):
    case_name : str
    request_body : Dict
    assert_case : List
    data_out : str = None

class BaseCaseUpdate(BaseModel):
    id : int
    case_name : str = None
    request_body : Dict = None
    assert_case : List = None
    data_out : str = None
