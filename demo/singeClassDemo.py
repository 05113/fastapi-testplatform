class single(object):


    instance = {}
    def __new__(cls, *args, **kwargs):
        if cls.instance == None:
            # 调用父类的__new__(cls)方法创建实例，并将该实例赋值给类变量instance，此时该变量的值从None变为该实例
            cls.instance = object.__new__(cls)
            # print cls.instance
            # 返回实例化对象
            return cls.instance
        else:
            # 返回上一个对象的引用
            return cls.instance

def single1(func):
    _instance = {}
    def wrapper(*args,**kwargs):
        if func in _instance:
            return _instance[func]
        else:
            _instance[func] = func(*args,**kwargs)
            return _instance[func]
    return wrapper
@single1
class k():
    def __init__(self):
        self.x = 10


a = single()
print(id(a))
b = single()
print(id(b))

l = k()
kk = k()
print(id(l))
print(id(kk))