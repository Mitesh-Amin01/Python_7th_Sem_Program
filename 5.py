try:
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero! You cannot divide by zero.")

except ValueError:
    print("Error: Invalid input! Please enter valid integer values.")

else:
    print("No exceptions were raised.")

finally:
    print("Execution completed.")

print("Program continues after exception handling.")
