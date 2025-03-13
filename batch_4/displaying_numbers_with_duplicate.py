print("Please enter 10 numbers")

num_list = []
for i in range (1,11):
    num = int(input(f"Number {i}: "))
    num_list.append(num)

duplicated_numbers = []
for num in num_list:
    if num_list.count(num) != 1:
        duplicated_numbers.append(num)

print(duplicated_numbers)