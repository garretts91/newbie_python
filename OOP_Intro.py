# Object oriented programming
#Go from general to specific to write good code

# def hello():
#     print("hello")

# print(type(hello))

#methods
#string = "hello"
#dot operators - methods acting upon specific objects
#method upper acting on the object type string
#print(string.upper())

#Classes are typically camelcase
class Dog:
    #method is a function that goes inside of a class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # print(name)

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def bark(self):
        print("woof")

d = Dog("Hunter", 8)
print(d.get_name())
d.set_age(500)
print(d.get_age())

d2 = Dog("Bodhi", 11)
print(d2.get_name())
print(d2.get_age())
# d.bark()
# print(type(d))

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        # self.is_active = False

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Student("Garrett", 31, 94)
s2 = Student("Trisha", 32, 98)
s3 = Student("Tim", 20, 83)

course = Course("Programming", 2)
course.add_student(s1)
course.add_student(s2)
print(course.students[0].name)
print(course.get_average_grade())


#with inheritance, parent initialization
#super() references the parent class (such as in the Cat class)
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what species of Pet I am.")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Woof")

class Fish(Pet):
    pass

#child classes are more specific and will override the initial definitions
p = Pet("Hunter", 8)
p.show()
c = Cat("Bill", 5, "Black")
c.show()
c.speak()
d = Dog("Bodhi", 11)
d.show()
d.speak()
f = Fish("Bubbles", 1)
f.speak()
# go from general to specific to write good code


#Class Attributes
#Make classes as robust as possible in order to be able to export your class to other data without dependencies, unless that is what you want dependencies
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Garrett")
p2 = Person("Trisha")
print(Person.number_of_people_())

#Static Method
class Math:

    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10
    
    @staticmethod
    def add15(x):
        return x + 15

    def pr():
        print("Run")

print(Math.add5(5))
Math.pr()

#Everything we work with is an object of some sort