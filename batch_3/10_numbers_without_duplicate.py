print("Please enter 10 numbers")

num_list = []
for i in range (1,11):
    num = int(input(f"Number {i}: "))
    num_list.append(num)

unique_numbers = []
for num in num_list:
    if num_list.count(num) == 1:
        unique_numbers.append(num)

print(unique_numbers)