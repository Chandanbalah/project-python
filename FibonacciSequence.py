N= int(input())
num1 = 0
num2 = 1
next_number = num2
count = 1
while count<=N:
    print(next_number)
    count+=1
    num1, num2 = num2,next_number
    next_number = num1+num2
