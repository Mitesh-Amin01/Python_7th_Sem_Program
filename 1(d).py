num1=int(input("Enter Number 1 :- "))
num2=int(input("Enter Number 2 :- "))

def check(num1,num2):
    gcd = 1
    for i in range(1,min(num1,num2)):
        if num1%i==0 and num2%i==0:
            gcd = i
            
    print("GCD is a ",gcd)
    
check(num1,num2)
            