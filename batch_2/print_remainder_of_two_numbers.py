print("Please enter two numbers")
num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    print(num1 % num2)