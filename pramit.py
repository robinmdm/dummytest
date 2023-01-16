# acceptable online resource:
#   - official python documentation
#   - w3schools python

# ---------------------------------------------------------------------------------------

# Challenge 1:

# # Given a list of names, write a Python program that groups the names that have the same set of characters and returns the grouped names in a list of lists.

# # names = [['PRAMIT'], ['SHUBHAM'], ['SWETHA'], ['ROLSTAN'], ['PRADEEP'], ['ROBIN']]

# # Output: [["PRADEEP", "PRAMIT"], ["ROBIN", "ROLSTAN"], ["SHUBHAM", "SWETHA"]]

# your code goes here

# XXXXXXXXXXXXXXXXX   DOES NOT WORK DO NOT READ   XXXXXXX


# names = [['PRAMIT'], ['SHUBHAM'], ['SWETHA'],
#          ['ROLSTAN'], ['PRADEEP'], ['ROBIN']]
# n = None
# lst1 = []
# for l in names:
#     if n is None:
#         n = []
#         n.append(l)
#         b = n[0]
#         c = b[0]
#     else:
#         a = l[0]
#         if a == c:
#             lst1.append(l)
#             n = None

# print(lst1)

# ---------------------------------------------------------------------------------------

# Challenge 2:

# # data = [1,[12,'a'],['b','c',4],[5,'d','d'],[50,5]]

# # Output: {"a": 50, "b": 12, "c": 5, "d": 4}

# your code goes here

# data = [1, [12, 'a'], ['b', 'c', 4], [5, 'd', 'd'], [50, 5]]
# data1 = []
# for i in data:
#     if isinstance(i, list) == True:
#         for j in i:
#             data1.append(j)
#     else:
#         data1.append(i)

# set1 = set(data1)
# data1 = list(set1)
# lst0 = []
# lst1 = []

# for i in data1:
#     if isinstance(i, int) == True:
#         continue
#     else:
#         lst0.append(i)

# set2 = set(lst0)
# set3 = set1-set2
# lst1 = list(set3)
# lst1.sort(reverse=True)
# lst0.sort()

# dict = {}

# for i in range(0, 4):
#     dict[lst0[i]] = lst1[i]

# print(dict)


# ------------------------------------------------------------------------------------------

# Challenge 3:

# # Finding all the Pythagorean triplets within a given range of numbers. (1, 10)

# # A Pythagorean triplet is a set of three positive integers, a, b and c, that satisfies the equation a^2 + b^2 = c^2.

# # output: 3 4 5
#           6 8 10

# your code goes here

# import math
# for i in range(1, 100):
#     for j in range(i+1, 100):
#         a = i**2+j**2
#         b = math.sqrt(a)
#         if b - int(b) == 0:
#             if b <= 100:
#                 print(i, j, int(b))


# ---------------------------------------------------------------------------------------------

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

# n = int(input("Enter value: "))
# j = 0
# for i in range(0, n):
#     print("#", end=" ")
#     print("&", end="")
#     for k in range(0, j):
#         print(" ", end="")
#     j += 1
#     print("&")

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

import math
n = int(input("Enter a number: "))

lst = []

for i in range(1, n+1):
    if i == 1:
        lst.append(i)
    else:
        str1 = ""
        for j in range(1, i+1):
            k = str(j)
            str1 += k
        s1 = str1[::-1]
        s2 = s1[1:]
        s3 = str1+s2
        t = int(s3)
        lst.append(t)

for i in range(0, n):
    print(" "*(n-i), end="")
    print(lst[i])
