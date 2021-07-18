class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name

class MyException(Exception):
    def __init__(self,ErrorInfo):
        super().__init__(self) #初始化父类
        self.errorinfo=ErrorInfo
    def __str__(self):
        if self.errorinfo == 'RedisNoConfigError':
            return 'redis 匹配不到项目配置'
        else:
            return 'server error'