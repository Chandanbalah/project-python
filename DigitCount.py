// Count no of digits
N= int(input())
quot = N
rmdr = 0
cntr=0 
while quot>=1:
    rmdr= quot%10
    quot = quot//10
    cntr+=1
print(cntr)
