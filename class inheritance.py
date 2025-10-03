import nis
from typing_extensions import self

class person:
    name = ""

    def __init__(self, name):
        self.name = name

    def getInfo(self):
        print("This person's name", self.name)

class student(person):
    pass

student1 = student("Ahmad")
student.getInfo()

def __init__(self, name, nis):
    self.name = name
    self.nis = nis

person1 = person("Ahmad")
student1 = student("Beni", "20211243")

def __init__(self, name, nis):
        super().__init__(name)
        self.nis = nis

person1  = person ("Ahmad")   
student1 = student("Beni", "20211243")

def study(subject):
        print(self.name, "is studying", subject)

student1 = student("Beni", "20211243")
student1.study("Math")           

def getInfo():
        print("this student's name is", self.name)

student1 = student("Beni", "20211243")
student1.getInfo()