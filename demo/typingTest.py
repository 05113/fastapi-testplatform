
# 会校验输入输出格式,如果不符合会报黄但不会报错
from typing import List,Dict

def a(a:List,b:List) -> List[int]:
    name:Dict[str] = {}
    return  a+b
def ttt(*,a:int ,b:int ) -> int:
    return a+b
if __name__ == '__main__':
    # k = ['l']
    # l = ['l']
    # b='1'
    # print(a(k,b))
    # a(k,l)
    print(ttt(1,2))