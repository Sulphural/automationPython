
class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1,2,3]

    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old")

    def change_age(self,age):
        self.age = age

    def add_weight(self, weight):
        self.weight = weight


tim = Dog("Tim", 45)
fred = Dog("Fred",85)
tim.change_age(5)
tim.add_weight(66)
fred.add_weight(444)
tim.speak()
fred.speak()

print(tim.weight)
print(fred.weight)