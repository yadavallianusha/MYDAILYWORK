class Animal:
    def __init__(self, name ,age):
        self.name = name
    def speak(self):
        print(self.name, "makes a sound")
      print("age:" self.age)
class Dog(Animal):
    def speak(self):
        print(self.name, "barks")
animal1 = Animal("Generic Animal")
dog1 = Dog("Rex",4)
animal1.speak()
dog1.speak()
