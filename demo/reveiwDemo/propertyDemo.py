class propertyDemo():
    def __init__(self,age):
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.setter
    def setAge(self,age):
        self.__age = age
if __name__ == '__main__':
    p = propertyDemo(3)
    print(p.age)
    p.setAge = 4
    print(p.age)
