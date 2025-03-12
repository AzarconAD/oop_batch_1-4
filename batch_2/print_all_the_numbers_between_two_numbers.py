num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

print(f"All the numbers between {num1} and {num2} are: ")

for i in range(num1 + 1, num2):
    print(i)