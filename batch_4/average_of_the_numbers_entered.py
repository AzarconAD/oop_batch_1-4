num_list = []

while True:
    try:
        num = int(input("Enter a number: "))
        num_list.append(num)

        sum_all = sum(num_list)
        print(sum_all)  

    except:
        ValueError
        break