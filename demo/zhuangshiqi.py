def kk():
    def bas(add_func):

        def insetFunc():

            return add_func() + "basketball"

        return insetFunc
    @bas
    def ll():
        return 'kkkk'

    print(ll())



# 被装饰函数不带参数
def budaicanshu():
    '''

    根据语法糖运行fun装饰器
    会先打印print('3')
    由于返回wrapper()函数,所以会接着调用wrapper()方法,
    由于wrapper方法会返回被装饰的函数,所以运行print('不带参数',f.__name__)之后接着调用被装饰的方法

    '''
    def fun(f):
        def wrapper():
            print('不带参数',f.__name__,f())
            return f()
        print('1')
        return wrapper

    @fun
    def no_can():
        print('nonocanshu')
        return 2
# 被装饰函数带参数
def daicanshu():
    def fun(f):
        def wrapper(*args,**kwargs):
            print('带参数',f.__name__)
            return f(*args,**kwargs)
        print('1')
        return wrapper

    @fun
    def kk(something):
        print('daidaidai参数',something)
        return 'kkk'

    kk('wang')
# 装饰器函数带参数
def zhuangshiqidaicanshu():
    def fun(level):
        def wrapper(func):
            def inner_wrapper(*args,**kwargs):
                print('dengji',level)
                # func(*args,**kwargs)
                return func(*args,**kwargs)
            return inner_wrapper
        return wrapper

    @fun(level='yilever')
    def kk(something):
        print('something',something)
        return 'kkk'
    kk('ssanyway')

if __name__ == '__main__':
    kk()
    budaicanshu()
    # daicanshu()
    zhuangshiqidaicanshu()