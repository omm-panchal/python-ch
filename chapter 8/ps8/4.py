"""
sum(1)=1
sum(2)=2 + 1
sum(3)=3 + 2 + 1
sum(4)=4 + 3 + 2 + 1


sum(n)= 1 + 2 +3 +4.....n
sum(n) = sum(n-1) + n
"""

def sum(n):
    if(n==1 ):
        return 1
    else:
      return sum(n-1) + n

print(sum(4))    
