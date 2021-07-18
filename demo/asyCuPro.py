
def cus():
    r = ''
    while True:
        n = yield r
        # if not n:
        print('xiaofeiyige',n)
        r='200 ok '

def pro(cus):
    cus.send(None)
    n = 0
    while n<5:

        print('shengchanyige',n)
        r = cus.send(n)
        print('xiaofeichenggong',r)
        n = n+1
        print()

if __name__ == '__main__':
    cus1 = cus()
    pro(cus1)
