# strNum = ["1","2","3"]

# jstrNum = ",".join(strNum)

# print(jstrNum)

# for item in jstrNum:
#     if item.isnumeric:
#         print(int(item)) 

the_numbers = input("please enter three numbers separated by a comma")

the_number_list = the_numbers.split(",")

the_sum = 0

for index, item in enumerate(the_number_list):
    print(index, item)
    if index == 0 or 1:
        the_sum = the_sum + int(item)
        print(the_sum)
    else:
        the_sum = the_sum - int(item)
        print(the_sum)