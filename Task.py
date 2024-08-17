#Task.1 Create a class named Person with the following properties/methods:Properties: first_name, last_name, age 
# Methods: display_info() - prints the values of all three properties.

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")

person1 = Person("Ahmad", "Ali", 30)
person1.display_info()
print("-------------------------")

#Task.2 Create a class named Student that inherits from the Person class. The Student class should have the following properties/methods:Properties: student_id, gpa
#Methods: display_info() - prints the values of all five properties

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, gpa):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.gpa = gpa

    def display_info(self):
        super().display_info()  
        print(f"Student ID: {self.student_id}")
        print(f"GPA: {self.gpa}")

student1 = Student("Taha", "Ahmad", 20, "12345", 3.8)
student1.display_info()
print("-------------------------")

#Task.3 Create a class named Teacher that inherits from the Person class. The Teacher class should have the following properties/methods:Properties: teacher_id, salary
#Methods: display_info() - prints the values of all five properties


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def __init__(self, first_name, last_name, age, teacher_id, salary):
        super().__init__(first_name, last_name, age)
        self.teacher_id = teacher_id
        self.salary = salary

    def display_info(self):
        super().display_info()  
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Salary: {self.salary}")

teacher1 = Teacher("Muhammad", "Arshad", 40, "98765", 50000)
teacher1.display_info()
print("-------------------------")

#Task.4 Create an instance of the Student class and call its display_info() method.
#Create an instance of the Teacher class and call its display_info() method.


class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, first_name, last_name, age, student_id, gpa):
        super().__init__(first_name, last_name, age)
        self.student_id = student_id
        self.gpa = gpa

    def display_info(self):
        super().display_info()  
        print(f"Student ID: {self.student_id}")
        print(f"GPA: {self.gpa}")

class Teacher(Person):
    def __init__(self, first_name, last_name, age, teacher_id, salary):
        super().__init__(first_name, last_name, age)
        self.teacher_id = teacher_id
        self.salary = salary

    def display_info(self):
        super().display_info() 
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Salary: {self.salary}")
student1 = Student("Ahmad", "Ali", 20, "12345", 3.8)
student1.display_info()
print()  
teacher1 = Teacher("Muhammad", "Arshad", 40, "98765", 50000)
teacher1.display_info()
print("-------------------------")