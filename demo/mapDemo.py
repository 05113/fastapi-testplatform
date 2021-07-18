# 利用map()函数，把用户输入的不规范的英文名字，
# 变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：

from functools import reduce

def f1(x,y):
    return x*y
def prod(L:list):
    result = reduce(f1,L)
    return result
def normalize(name:str):
    re_name = name.lower().capitalize()
    return re_name
if __name__ == '__main__':
    strlist = ['adam', 'LISA', 'barT']
    r = map(normalize,strlist)
    print(list(r))

    listint = [1,2,3,4]
    r = prod(listint)
    print(r)