Maths = int(input("enter your marks of maths out of 100 :"))
Science = int(input("enter your marks of science out of 100 :"))
English = int(input("enter your marks of english out of 100 :"))

total_percentage = (100*(Maths + Science + English)/300)

if (Maths>100 and Science>100 and English>100) :
    print("plz enter valid marks out of 100")

if (total_percentage>=40 and Maths>=33 and Science>=33 and English>=33) :
    print("you are pass, good job :", total_percentage)    

else:
    print("you are fail , better luck next time :" , total_percentage )    


print("its student's percentile of 3 main subjects")