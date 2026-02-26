class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print(self.name, "makes a sound")
        print("Age:", self.age)
class Dog(Animal):
    def speak(self):
        print(self.name, "barks")
        print("Age:", self.age)
animal1 = Animal("Generic Animal", 5)
dog1 = Dog("Rex", 4)
animal1.speak()
dog1.speak()
