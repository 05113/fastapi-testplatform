'''
如果产生异常会执行except块
finally铁定会被执行
'''

import os
import sys
from demo.myexcpt import MyException
from common.logger import logger,error

try:
    print("try")
except:
    print("except")
finally:
    print("finally")
print('---------------------')
try:
    print("try")
    raise 1
except:
    print("except")
finally:
    print("finally")
print("-------------")

def a():
    l ={}
    try:
        k = l['kk']
    except :
        raise MyException('no kk')

def b():
    try:
        m = a()
    except MyException as e :
        print(e.__str__())
    finally:
        print(2)

# b()

def c():
    try:
        ll = {}
        a = ll['kkcc']
        # a = 1/0
    except KeyError as e:
        logger.error(error(filename=os.path.basename(__file__), fileline=sys._getframe().f_lineno))
        print(e.__str__())

c()


