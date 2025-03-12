print("Please enter two numbers")
num1 = float(input("1st number: "))
num2 = float(input("2nd number: "))
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    print(num1 % num2)