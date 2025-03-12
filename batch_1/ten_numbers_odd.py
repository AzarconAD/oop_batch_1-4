print("Please enter ten numbers.")
odd_count = sum(1 for i in range(1, 11) if float(input(f"Number {i}: ")) % 2 != 0)
print(f"{odd_count} numbers are odd.")