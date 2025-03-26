print("(Enter an invalid input to exit.)")
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

# better code
# nums = {}
# while True:
#       try:
#           num = int(input("enter a number: "))
#           if nums.get(num):
#              nums[num] += 1
#           else:
#              nums[num] = 1
#       except:
#           break
#
# biggest = max(nums.values())
# for i in nums.keys():
#     if nums[i] == biggest:
#       print(i)