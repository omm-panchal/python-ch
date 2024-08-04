class Student:   
    language = "Python"
    Marks = 88

    def getinfo(self):
        print(f"Language is: {self.language}, Marks is: {self.Marks}")
    @staticmethod
    def greet():
        print("Thank you")
om = Student()

om.getinfo() 
#Student.getinfo(om)
om.greet() 