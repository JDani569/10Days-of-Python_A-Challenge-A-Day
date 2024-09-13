# Task 1
# Write a function called string_range that takes a single
# number and returns a string of its range. The string characters
# should be separated by dots(.) For example, if you pass 6 as
# an argument, your function should return ‘0.1.2.3.4.5’.

a = int(input("Enter your value: "))

for i in range(0,a):
    print(f"{i}",end=".")

# Task 2
# You are given a list of names, and you are asked to write a code
# that returns all the names that start with ‘S’. Your code should
# return a dictionary of all the names that start with S and how
# many times they appear in the dictionary. Here is a list below:
names = ["Joseph","Nathan", "Sasha", "Kelly", "Muhammad", "Jabulani", "Sera", "Patel", "Sera"]
dic = {}

for i in names:
    if i[0] == 'S':
        key = i
        value = names.count(i)
        dic[key] = value
print(dic)