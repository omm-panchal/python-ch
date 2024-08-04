class Programmer:
    Company = "Microsoft"
    def __init__(self, name, Experience, Salary):
        self.name = name
        self.Experience = Experience
        self.Salary = Salary


p =Programmer("om", "Fresher", 50000)
print(p.name,p.Experience,p.Salary)

pranjal =Programmer("Pranjal", "Fresher", 500000)
print(pranjal.name,pranjal.Experience,pranjal.Salary)