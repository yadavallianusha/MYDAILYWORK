class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def show_student_details(self):
        self.show_person_details()
        print("Marks:", self.marks)

        if self.marks >= 35:
            print("Result: Pass")
        else:
            print("Result: Fail")
student1 = Student("Anusha", 22, 78)
student2 = Student("Ravi", 21, 30)
print("Student 1 Details")
student1.show_student_details()

print("\nStudent 2 Details")
student2.show_student_details()
