#pattern of factorial ex ( 5!  = 1 x 2x 3x 4x 5)


n = int(input("enter number: "))
product = 1

for i in range(1, n+1) :
    
    product = product * i

print(f"the factorial of {n} is {product}")