import random
x1 = 1 
x2 = 100 
n = 0 
a = random.randint(x1,x2) 
while True: 
    answer = int(input()) 
    if answer == a: 
        print("正確") 
        print("已經猜了",n,"次")
        break 
    elif answer < a: 
        print("太低了") 
        n = n+1 
    elif answer > a: 
        print("太高了") 
        n = n+1
