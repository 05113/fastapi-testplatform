import sys
import os
import types

a = ['1','2','3']
k = a[1:]
print(k)

l = [
    {"assert_key": "response.success", "assert_value": True, "comparison_operator": "equal"},{"assert_key": "response.code", "assert_value": "300", "comparison_operator": "equal"}
  ]

print(type(l))

print(sys._getframe().f_lineno)
code = '替换url异常-异常文件名:{}-异常代码行数:{}'.format(os.path.basename(__file__),sys._getframe().f_lineno)
print(code)


a = [1,5,7,9]
b = [2,2,3,10]
# extend合并
a.extend(b)
print(a)
a.sort(reverse=False)
print(a)

a = [2]
print(a[2:])

s = [1,2,3,4,5]

s[1] = s[3]
print(s)

# print(next(range(10)))
print(isinstance([i for i in range(10)], list))

ss = [1,2,3]
if ss.pop() == 3:
    print('111,wang')
print(ss)