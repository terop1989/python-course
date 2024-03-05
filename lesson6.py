class Animal:
    def voice(self):
        pass

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