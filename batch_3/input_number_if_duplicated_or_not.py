while True:
    try: 
        entered_number = int(input("Input a number: "))
    except:
        ValueError
        print("invalid input!")
        break
    