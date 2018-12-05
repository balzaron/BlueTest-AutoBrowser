import json

class Person(object):

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        self.__sex = sex


p = Person()
p.name = 'lolo'
print(p.name)


s = json.dumps(p.__dict__) # s set to: {"x":1, "y":2}
o = json.loads(s)
print(s)