num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

        sorted_list = sorted(num_list)
        print(sorted_list[0])
    except:
        ValueError
        break