import datetime
import decimal
import json
from typing import Union
import re
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
        obj_list = []
        for u in obj:
            dict = u.__dict__
            # 去掉__dict__中的_sa_instance_state属性
            dict.pop('_sa_instance_state',None)
            obj_list.append(dict)
        return json.loads(json.dumps(obj_list,default=_alchemy_encoder))
    else:
        # 转换fetchone()后的对象
        return json.loads(json.dumps(dict(obj), default=_alchemy_encoder))

def re_sub_url(url : str , config : dict):
    pattern = r'{(.*?)}'
    re_list = re.findall(pattern = pattern , string = url)
    if len(re_list) == 0:
        return url
    else:
        for item in range(len(re_list)):
            value = config[re_list[item]]
            # 第一个参数对应的正则表达式，第二个参数为要替换成的字符串，第三个参数为源字符串，第四个参数为可选项，代表最多替换的次数，如果忽略不写，则会将符合模式的结果全部替换。
            url = re.sub(r'{.*?}' , value , url,1)

        return url

if __name__ == '__main__':
    aa = {}
    aa['aaa'] = '1'
    aa['bbb'] = '2'

    print(re_sub_url('www.baidu.com',aa))