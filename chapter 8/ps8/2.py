"""
c/5 = (f-32)/9
"""

c = int(input("Enter temperature in celcius "))

def ctof (c):
    
    f = ((9*c)/5)+32
    return f
print(f"answer is : {ctof(c)}","in Farheinit")