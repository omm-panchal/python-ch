class Student:   
    language = "Python"
    Marks = 88

    def __init__(self): #dunder methnod
        print("I am creating an object")

    def getinfo(self):
        print(f"Language is: {self.language}, Marks is: {self.Marks}")

om = Student()

om.name ="om"
print(f"name is: {om.name}, Language is: {om.language}, Marks is: {om.Marks}")
