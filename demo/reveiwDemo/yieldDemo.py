def k(n):
    print('jhhhh')
    if n:
        print('ok',n)
    yield n
    print('1')



l = k(3)
print(next(l))
l.send(4)

