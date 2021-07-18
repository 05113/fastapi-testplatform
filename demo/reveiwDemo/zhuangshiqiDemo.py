# 无参数装饰器
def log(fun):
    def wrapper():
        print('hhh')
        return fun()
    return wrapper
@log
def kk():
    print('xxx')
# kk()

# 有参数装饰器
def argfun(fun):
    def wrapper(*args,**kwargs):
        print('wang',*args,**kwargs)
        return fun(*args,**kwargs)
    return wrapper
@argfun
def aa(something):
    print(something)
    return something+1
# b = aa(3)
# print(b)

# 装饰器带参数
def ff(*args,**kwargs):
    if args == 'level':
        print('level',args)
    else:
        print('no level',args)
    def wrapper(fun):
        print('装饰器逻辑')
        def inner_wrapper(*args,**kwargs):
            return fun(*args,**kwargs)
        return inner_wrapper
    return wrapper
@ff('mmm')
def m(something):
    print('wangq',something)
lll = m(3)
