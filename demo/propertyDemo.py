class Sou(object):
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self,value):
        self._age = value
    @property
    def bir(self):
        return self._age+1
if __name__ == '__main__':
    s = Sou()
    s.age = 10
    print(s.bir)