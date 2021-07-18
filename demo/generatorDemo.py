g = (x * x for x in range(10))
print(g)


def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))

l = [x * x for x in range(10)]
k = iter(l)
print(next(k))
print(next(k))

