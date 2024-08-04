age = int(input("plz enter your age : "))
#statement no.1 starts
if(age>= 18) :
    print("you are an adult ")
    print("you are now able to enjoy your 18+ rights ")



elif(12<age<18) :
    print("You are a teenager , you are in an growing age")

elif(age<0) :
    print("you entered invalid age ")

#^
#indentation space that you are in if/else too     
else :
    
    print("you are minor ")
#statement no.1 ends

if(age%2 == 0) :
    print("age is even")

print("End of program")