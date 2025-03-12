print("Please enter ten numbers")
num_list = [float(input(f"Number {i}: ")) for i in range(1, 11)]
print(f"The sum of all ten numbers is {sum(num_list)}.")