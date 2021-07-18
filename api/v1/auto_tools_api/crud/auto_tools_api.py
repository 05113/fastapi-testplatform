import time
import json
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.tools_func import serialize_sqlalchemy_obj


class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj,datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self,obj)



class CRUDToolsApi():
    def __init__(self):
        pass
    def sleep_fun(self , sleeptime : dict):
        sleeptime = sleeptime['sleeptime']

        time.sleep(sleeptime)

    def sql_fun(self , sql_info:dict):
        username = sql_info['username']
        password = sql_info['password']
        host = sql_info['host']
        port = sql_info['port']
        database = sql_info['database']
        sql = sql_info['sql']
        database_url = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}?charset=utf8mb4"

        engine = create_engine(database_url , pool_pre_ping = True)
        DbSession = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

        session = DbSession()

        if 'select' in sql.lower():
            data_response = []
            cursor = session.execute(sql)
            result = cursor.fetchall()
            # data_response = serialize_sqlalchemy_obj(result)
            for rowproxy in result:
                dict = {}
                for column , value in rowproxy.items():
                    if isinstance(value , datetime.datetime):
                        value = value.strftime("%Y-%m-%d %H:%M:%S")
                    dict[column] = value
                    data_response.append(dict)
            return data_response



crud_tools_api = CRUDToolsApi()