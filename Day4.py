# Task 1
# Write a function called only_floats, which takes two
# parameters a and b, and returns 2 if both arguments are floats,
# returns 1 if only one argument is a float, and returns 0 if neither
# argument is a float. If you pass (12.1, 23) as an argument, your
# function should return a 1.

# a = 12.1
# b = 23

# # method 1
# if f"{type(a)}" == "<class 'float'>" and f"{type(b)}" == "<class 'float'>":
#     print(2)
# elif f"{type(a)}" == "<class 'float'>" or f"{type(b)}" == "<class 'float'>":
#     print(1)
# else:
#     print(0)

# # method 2
# if isinstance(a,float) and isinstance(b,float):
#     print(2)
# elif isinstance(a,float) or isinstance(b,float):
#     print(1)
# else:
#     print(0)

# Task 2
# Write a function called word_index that takes one argument,
# a list of strings and returns the index of the longest word in the
# list. If there is no longest word (if all the strings are of the same
# length), the function should return zero (0). For example, the list
# below should return 2.

word1 = ["Hate", "remorse", "vengeance"]
b = []
word2 = ["Love", "Hate"]

a = 0
for i in word1:
    b.append(len(i))
    if a < len(i):
        a = len(i)
print(a)
print(b)