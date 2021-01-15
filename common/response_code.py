from typing import Union , Dict
from fastapi import status
from fastapi.responses import JSONResponse , Response

# * 号， 意思是调用的时候要指定参数 e.g.resp_200（data=xxxx),如果不指定参数会报错

def resp_200(*,data : Union[list , dict , str ] = None , message : str = 'success') -> Response :
    return JSONResponse(
        status_code = status.HTTP_200_OK,
        content= {
            'code' : 200,
            'message' : message,
            'data' : data
        }
    )

def resp_500(*, data : Union[list , dict , str ] = None , message : str = 'server error ') -> Response:
    return JSONResponse(
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
        content = {
            'code' : 500,
            'message' : message,
            'data' : data
        }
    )

