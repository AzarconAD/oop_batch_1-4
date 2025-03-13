while True:
    try: 
        num_list = [int(input("Input a number: "))]

        unique_numbers = []
        for num in num_list:
            if num_list.count(num) == 1:
                print("Unique")
                unique_numbers.append(num)
                if num_list.count(num) != 1:
                    print("Duplicate")

    except:
        ValueError
        print("invalid input!")
        break
    