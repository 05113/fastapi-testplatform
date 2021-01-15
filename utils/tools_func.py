import datetime
import decimal
import json
from typing import Union
def _alchemy_encoder(obj):
    """
    处理序列化中的时间和小数
    :param obj:
    :return:
    """
    if isinstance(obj, datetime.date):
        return obj.strftime("%Y-%m-%d %H:%M:%S")
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

def serialize_sqlalchemy_obj(obj) -> Union[dict, list]:
    """
    序列化fetchall()后的sqlalchemy对象
    https://codeandlife.com/2014/12/07/sqlalchemy-results-to-json-the-easy-way/
    :param obj:
    :return:
    """
    if isinstance(obj, list):
        # 转换fetchall()的结果集
        obj = [ u.__dict__ for u in obj ]
        return json.loads(json.dumps(obj,default=_alchemy_encoder))
    else:
        # 转换fetchone()后的对象
        return json.loads(json.dumps(dict(obj), default=_alchemy_encoder))