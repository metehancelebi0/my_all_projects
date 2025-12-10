# File Processing and Conditional Selection

# def score_len(textfile):
#     with open(textfile, "r") as f:
#         for line in f:
#             parts = line.split()
#             name = parts[0]
#             scores = parts[1:]
#             if len(scores) > 6:
#                 print(name)
#
# score_len("studentdata(1).txt")



# Operator Overload

# list1 = [1,2,3,4]
# list2 = [5,6,7,"Red"]
#
# final_list = list1 + list2
# print(final_list)



# Finding Common Elements with Loops and Conditions

# list_a = [1,2,3,4,5]
# list_b = [3,4,5,6,7]
#
# for elem in list_a:
#     if elem in list_b:
#         print(elem)



# Palindrome Check

# def control_list(list):
#     if list == list[::-1]:
#         return True
#     return False
#
# a_list = [1,2,3,2,1]
# print(control_list(a_list))



# Finding the Second Largest Element

# def find_second(lst):
#     largest = max(lst)
#     second = None
#     for item in lst:
#         if item != largest:
#             if second is None or item > second:
#                 second = item
#     return second
#
# print(find_second([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))



# Range Control

# def return_function(lst):
#     for elem in lst:
#         if 10 <= elem <= 50:
#             print(elem)
#
# a_list = [7,8,15,32,48,50,60,92]
# return_function(a_list)








