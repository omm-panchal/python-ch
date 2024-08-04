class Student:   #Empty form
    Subject = "Python" # This is an class attribute
    Marks = 88

Om = Student() #Filled form And Object
Om.name= "om" # This is an Object/Instance attribute
print(Om.name, Student.Subject, Student.Marks)

# Here name is Object attribute and Subject and Marks are class attributes as they belong to class

class Student:   #Empty form
    Subject = "Python"
    Marks = 88

Student() #Filled form And Object
Student.name= "om"
print(Student.name, Student.Subject, Student.Marks)
