'''class student:
    def __init__(s, name, marks):
        s.name = name
        s.marks = marks
    def display(self):
        print(f"student name: {self.name}")
        print(f"student marks: {self.marks}")
name =str(input("enter the name:"))
marks=int(input("enter the marks:"))
s= student(name,marks)
s.display()'''

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @classmethod
    def input(cls):
        name = str(input("enter the name:"))
        marks = int(input("enter the marks:"))
        return cls(name, marks)
    def display(self):
        print(f"student name: {self.name}")
        print(f"student marks: {self.marks}")
s = student.input()
s.display()

