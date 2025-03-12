print("Please enter 10 numbers")

num_list = []
for i in range (1,11):
    num = int(input(f"Number {i}: "))
    if num not in num_list:
        num_list.append(num)

print(num_list)