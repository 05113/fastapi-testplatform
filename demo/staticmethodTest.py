class C():
    # 声明静态方法
    @staticmethod
    def a():
        print(1)
if __name__ == '__main__':
    # 静态方法无需实例化
    C.a()
    # 也可实例化调用
    k = C()
    k.a()