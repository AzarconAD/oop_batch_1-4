num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

        sum_all = sum(num_list)
        length = len(num_list)
        average = sum_all / length
        print(average)

    except:
        ValueError
        break