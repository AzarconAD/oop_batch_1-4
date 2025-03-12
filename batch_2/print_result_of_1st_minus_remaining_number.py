print("Please enter ten numbers")
num_list = [float(input(f"Number {i}: ")) for i in range(1, 11)]

result = num_list[0]
for num in num_list[1:]:
    result -= num

print(f"The difference of 1st number over the remaining numbers is {result}.")