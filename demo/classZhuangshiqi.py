class A(object):
    def __init__(self):
        print ("77777")

def decorator1(cls):
    cls.test_val = 1
    return cls

@decorator1
class Model(object):
    test_val = 0
    def __init__(self):
        print ("model created")

if __name__ == '__main__':
    model = Model()
    print (model.test_val)