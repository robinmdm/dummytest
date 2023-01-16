# acceptable online resource:
#   - official python documentation
#   - w3schools python

#---------------------------------------------------------------------------------------

# Challenge 1:

# # Given a list of names, write a Python program that groups the names that have the same set of characters and returns the grouped names in a list of lists.

# # names = [['PRAMIT'], ['SHUBHAM'], ['SWETHA'], ['ROLSTAN'], ['PRADEEP'], ['ROBIN']]

# # Output: [["PRADEEP", "PRAMIT"], ["ROBIN", "ROLSTAN"], ["SHUBHAM", "SWETHA"]]
# your code goes here
names = [['PRAMIT'], ['SHUBHAM'], ['SWETHA'], ['ROLSTAN'], ['PRADEEP'], ['ROBIN']]
output = []
condition = True
temp = []
for i in range(0,(len(names))):
    for j in range(0, len(names)):        
        if((names[i][0][0] == names [j][0][0]) and (i != j)):
            temp = []
            temp.append(names[i][0])
            temp.append(names[j][0])
            output.append(temp)
output = sorted(output)
final = []
for i in range(0,len(output),2):
    final.append(output[i])
print(final)






# ---------------------------------------------------------------------------------------

# Challenge 2:

# # data = [1,[12,'a'],['b','c',4],[5,'d','d'],[50,5]]

# # Output: {"a": 50, "b": 12, "c": 5, "d": 4}

# your code goes here

# data = [1,[12,'a'],['b','c',4],[5,'d','d'],[50,5]]

# list1 = []

# for d in data:
#     if(type(d) != list):
#         list1.append(d)
#     elif(type(d) == list):
#         for k in d:
#             list1.append(k)

# numbers = []
# alphabets = []
# for l in list1:
#     if(type(l) == int):
#         numbers.append(l)
#     else:
#         alphabets.append(l)

# numbers.sort(reverse=True)
# # print(numbers)

# alphabets.sort()
# # print(alphabets)

# dict = {}
# dict = dict.fromkeys(alphabets)
# i = 0
# for key in dict:
#     dict [key] = numbers[i]
#     i+=1 
# print(dict)
# ------------------------------------------------------------------------------------------

# Challenge 3:

# # Finding all the Pythagorean triplets within a given range of numbers. (1, 10)

# # A Pythagorean triplet is a set of three positive integers, a, b and c, that satisfies the equation a^2 + b^2 = c^2.

# # output: 3 4 5
#           6 8 10

# your code goes here

# ls = []
# mls = []
# for i in range (1,100):
#     for j in range(1,100):
#         for k in range(1,100):
#             if j**2 + k**2 == i**2:
#                 ls = []
#                 ls.append(i)
#                 ls.append(j)
#                 ls.append(k)
#                 mls.append(ls)

# cls = []
# # for e in mls:
# #     for i in e:


# #         print(i," ",end="")
# #     print()

# for e in mls:
#     e.sort()

# for i in range(0,len(mls)):
#     for j in range(0,len(mls),2):
#         if ((i != j) and mls[i]==mls[j]):
#             for m in mls[i]:
#                 print(m," ",end="")
#             print()



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



# n = int(input("enter the number of rows"))
# print("&&")
# for s in range(0,n-1):
#     print("&"," "*s,"&")
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
# str = ""
# n = int(input("enter the number of rows"))

# print(str)



# s = n
# for i in range(0,n):
#     j = 0
#     midstr = ""
#     for j in range (0,i):
#         j.__
    




#     print(" "*s-1,i," "*s-1)
#     s = s - 1