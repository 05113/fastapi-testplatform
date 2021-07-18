def kk():
    try:
        k = 1
        print('wang')
        yield k
    finally:
        print('quan')

s = kk
print(s)