class Animal:
    num_of_childs = 0

    def __init__(self):
        Animal.num_of_childs = Animal.num_of_childs + 1

    def voice(self):
        pass

    def count():
        print(Animal.num_of_childs)
    count = staticmethod(count)


class Animal1(Animal):
    def voice(self):
        print("custom class 1")

class Animal2(Animal):
    def voice(self):
        print("custom class 2")

class Animal3(Animal):
    def voice(self):
        print("custom class 3")


a1 = Animal1()
a1.voice()

a2 = Animal2()
a2.voice()

a3 = Animal3()
a3.voice()
a3.count()