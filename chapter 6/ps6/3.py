p1 = "make a lot of money"
p2 = "click here"
p3 = "buy now"
p4 = "this is my insta id"

message = input("Enter your comment : ")

if(p1 in message or p2 in message or p3 in message or p4 in message) :
    print("this comment is spam")

else:    
    print("this comment is not a spam")