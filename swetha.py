# acceptable online resource:
#   - official python documentation
#   - w3schools python

# ---------------------------------------------------------------------------------------

# Challenge 1:

# # Given a list of names, write a Python program that groups the names that have the same set of characters and
# returns the grouped names in a list of lists.

# # names = [['PRAMIT'], ['SHUBHAM'], ['SWETHA'], ['ROLSTAN'], ['PRADEEP'], ['ROBIN']]

# # Output: [["PRADEEP", "PRAMIT"], ["ROBIN", "ROLSTAN"], ["SHUBHAM", "SWETHA"]]

# your code goes here

# ---------------------------------------------------------------------------------------

# names = [['PRAMIT'], ['SHUBHAM'], ['SWETHA'], ['ROLSTAN'], ['PRADEEP'], ['ROBIN']]
# names_sorted = sorted(names)
# new_list = []
# for x in names_sorted:
#     if type(x) is list:
#         for y in x:
#             new_list.append(y)
#     else:
#         new_list.append(x)
# print(new_list)

# for num in range(0,1):
#     new_dict = {new_list[num]: new_list[num+1], new_list[num+2]: new_list[num+3], new_list[num+4]: new_list[num+5]}
# print(new_dict)

# Challenge 2:

# # data = [1,[12,'a'],['b','c',4],[5,'d','d'],[50,5]]

# # Output: {"a": 50, "b": 12, "c": 5, "d": 4}

# your code goes here

# data = [1, [12, 'a'], ['b', 'c', 4], [5, 'd', 'd'], [50, 5]]
# my_dict = {}
# new_list = []
# string_variable = []
# integer_variable = []
# for x in data:
#     if type(x) is list:
#         for y in x:
#             new_list.append(y)
#     else:
#         new_list.append(x)
# print(new_list)
# for var in new_list:
#     if type(var) is str:
#         string_variable.append(var)
#     elif type(var) is int:
#         integer_variable.append(var)
# integer_variable.sort()
# integer_variable.reverse()
# for length in range(0, len(string_variable)):
#     my_dict[string_variable[length]] = integer_variable[length]
# print(my_dict)

# ------------------------------------------------------------------------------------------

# Challenge 3:

# # Finding all the Pythagorean triplets within a given range of numbers. (1, 10)

# # A Pythagorean triplet is a set of three positive integers, a, b and c, that satisfies the equation a^2 + b^2 = c^2.

# # output: 3 4 5
#           6 8 10

# your code goes here

# ---------------------------------------------------------------------------------------------

range_var = 11
for x in range(1, range_var):
    for y in range(1, range_var):
        for z in range(1, range_var):
            x_sqr_plus_y_sqr = int(x ** 2) + int(y ** 2)
            z_sqr = int(z ** 2)
            if x_sqr_plus_y_sqr == z_sqr:
                print(x, y, z)

# Challenge 4:

# Write a program using nested loops to draw this pattern.

# User will enter the number of rows.

# For, given input 6. The output will be:

# &&
# & &
# &  &
# &   &
# &    &
# &     &

# For, given input 10. The output will be:

# &&
# & &
# &  &
# &   &
# &    &
# &     &
# &      &
# &       &
# &        &
# &         &

# your code goes here

# input_number = int(input("Enter a number: "))
# for i in range(1, input_number+1):
#     if i == 1:
#         print("&"*2)
#     elif i == 2:
#         print("& &")
#     else:
#         print("&", " " * int(i - 2), "&")


# --------------------------------------------------------------------------------------------------

# challenge 5

# For given number of rows print this pattern

# For input 5, the output will be:

#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1

# For input 9, the output will be:

#                 1
#               1 2 1
#             1 2 3 2 1
#           1 2 3 4 3 2 1
#         1 2 3 4 5 4 3 2 1
#       1 2 3 4 5 6 5 4 3 2 1
#     1 2 3 4 5 6 7 6 5 4 3 2 1
#   1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

# your code goes here

# input_number = int(input("Enter a number: "))

# for num in range(0, input_number):
#     print(num, range(num+1) * num, num)

