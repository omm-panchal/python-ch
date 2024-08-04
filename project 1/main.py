import random
"""
snake = 1
water = -1
gun = 0

"""
computer =random.choice([1,-1,0])

rules = "s==> snake", "w==> water", "g==> gun"
print("rules of game are: ",rules)
youstr = input("Enter your choice: ")
youdict={"s" : 1,
         "w" : -1,
         "g" : 0,
         }
reversedict={1:"snake",
            -1:"water",
             0:"gun"
         }
you = youdict[youstr]


print(f"You chose: {reversedict[you]}\nThe computer chose: ",reversedict[computer])

if(computer == you):
    print("it's a draw")
else:
    if(computer==1 and you==-1)    :
        print("you lost, snake drunk water")

    elif(computer==1 and you==0)    :
        print("you won, gun killed snake")

    elif(computer==-1 and you==1)    :
        print("you won, snake drunk water")

    elif(computer==-1 and you==0)    :
        print("you lost, gun drowned in water" )

    elif(computer==0 and you==1)    :
        print("you lost, gun killed snake")

    elif(computer==0 and you==-1)    :
        print("you won, gun drowned in water")

    else:
        print("something went wrong")