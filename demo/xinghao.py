
def a(*,k,l):
    return k+l
def b(k,*,c):
    return k+c
# def c(...,a=1,c=2):



if __name__ == '__main__':
    # a(1,2) 不指定参数会报错
    print(a(k=1,l=2))
    # 必须指定*后边的参数
    print(b(1,c=2))

    for item in range(0):
        print("a")

