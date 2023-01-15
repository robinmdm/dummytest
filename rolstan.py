# acceptable online resource:
#   - official python documentation
#   - w3schools python

#---------------------------------------------------------------------------------------

# Challenge 1:

# # Given a list of names, write a Python program that groups the names that have the same set of characters and returns the grouped names in a list of lists.

# # names = [['PRAMIT'], ['SHUBHAM'], ['SWETHA'], ['ROLSTAN'], ['PRADEEP'], ['ROBIN']]

# # Output: [["PRADEEP", "PRAMIT"], ["ROBIN", "ROLSTAN"], ["SHUBHAM", "SWETHA"]]

# your code goes here

# ---------------------------------------------------------------------------------------

# Challenge 2:

# # data = [1,[12,'a'],['b','c',4],[5,'d','d'],[50,5]]

# # Output: {"a": 50, "b": 12, "c": 5, "d": 4}

# your code goes here

# ------------------------------------------------------------------------------------------

# Challenge 3:

# # Finding all the Pythagorean triplets within a given range of numbers. (1, 10)

# # A Pythagorean triplet is a set of three positive integers, a, b and c, that satisfies the equation a^2 + b^2 = c^2.

# # output: 3 4 5
#           6 8 10

output = []

filteredOutput = []

finalOutput = []

for i in range(1, 11):

    for j in range(1, 11):

        for k in range(1, 11):

            a = i**2

            b = j**2

            c = k**2

            if a + b == c:

                output.append([i, j, k])


for i in range(len(output)):
    filteredOutput.append(sorted(output[i]))

for i in filteredOutput:

    if i not in finalOutput:

        finalOutput.append(i)

for i in finalOutput:

    for j in i:

        print(str(j), end=" ")

    print()

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

n = int(input('Enter a number...'))

separatorIndex = 1

for i in range(n):

    for j in range(n+1):

        if int(j) == int(0):
            print('&', end="")
        elif int(j) == int(separatorIndex):
            print('&', end="")
        else:
            print(' ', end="")

    print()
    separatorIndex += 1

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
