num1=int(input("Enter Number 1 :- "))
num2=int(input("Enter Number 2 :- "))


def check(num1,num2):
    for num in range(num1, num2 + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
        
check(num1,num2)  