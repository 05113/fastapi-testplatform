def kk(l:list,n):
    res = []
    for _ in range(n):
        a = l.pop()
        res.append(a)
    res = res[::-1]
    res.extend(l)
    return res

l = ['a','b','c','d','e','f','g']
print(kk(l,4))