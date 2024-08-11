user_input = input("Enter Your Number :- ")

def check(num):
    length = int(len(num))
    ans = 0
    for i  in num:
        a=int(i)
        ans += a**length
    num = int(num)
    if num == ans:
        print("Number is a Armstrongc :- ",num)
    else:
        print("Number is a not Armstrong :- ",num)
check(user_input)
    