marks = int(input("enter marks out of 100 : "))


if(90<marks<=100 )    :
    print("You achieved ex grade")
    
elif(80<marks<=90 )    :
    print("You achieved A grade")

elif(70<marks<=80 )    :
    print("You achieved B grade")   

elif(60<marks<=70 )    :
    print("You achieved C grade") 

elif(50<marks<=60 )    :
    print("You achieved D grade")        

else  :
    print("you achieved F grade")    


if ( marks < 0 or marks > 100) :
    print("invalid marks, please re-enter marks out of 100")    