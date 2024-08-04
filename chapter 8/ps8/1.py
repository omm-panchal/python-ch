a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))


def greatest(a,b,c):
    if(a>b and a>c) :
        return f"Greatest number is {a}" 
    elif(b>c and b>a):
        return f"Greatest number is {b}" 
    elif(c>b and c>a):
        return f"Greatest number is {c}" 
    


print(f"{greatest(a,b,c)}") 