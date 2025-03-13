num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

    except:
        ValueError
        break

if num_list:
    frequency = {}
    for num in num_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    most_common_num = max(frequency, key=frequency.get)
    print(f"The most duplicated number is: {most_common_num}")