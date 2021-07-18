def feibonaqi(n):
    a ,b = 0,1
    res = []
    res.append(0)
    for _ in range(n):
        a,b = b , a+b
        res.append(a)
    return res

print(feibonaqi(3))