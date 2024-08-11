user_input = int(input("Enter Your Number :- "))

def check(a):
    if a%2 == 0:
        print("Even Number :- ",a)
    else:
        print("Odd Number :- ",a)

check(user_input)