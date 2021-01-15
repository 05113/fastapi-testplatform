# -*- coding: utf-8 -*-


class A(object):
    """
    Class A.
    """

    a = 0
    b = 1

    def __init__(self):
        self.a = 2
        self.b = 3

    def test(self):
        print ('a normal func.')

    @staticmethod
    def static_test(self):
        print ('a static func.')

    @classmethod
    def class_test(self):
        print ('a calss func.')


obj = A()
print (A.__dict__)
print (obj.__dict__)