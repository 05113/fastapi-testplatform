def singe(fun):
    __instance = {}
    def wrapper(*args,**kwargs):
        if fun in __instance:
            return __instance[fun]
        else:
            __instance[fun] = fun(*args,**kwargs)
            return __instance[fun]
    return wrapper

@singe
class a():
    def __init__(self):
        x =1
l = a()
m = a()

print(id(l))
print(id(m))