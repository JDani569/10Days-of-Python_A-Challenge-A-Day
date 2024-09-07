# Task 1
# Write a function called convert_add that takes a list of strings
# as an argument and converts it to integers and sums the list. For
# example [‘1’, ‘3’, ‘5’] should be converted to [1, 3, 5] and
# summed to 9.
import PSreadLine

a = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
b = 0
for i in a:
    b += int(i)
print("Sum is: ", b)

# Task 2
# Write a function called check_duplicates that takes a list of
# strings as an argument. The function should check if the list has
# any duplicates. If there are duplicates, the function should return
# the duplicates. If there are no duplicates, the function should
# return "No duplicates". For example, the list of fruits below
# should return apple as a duplicate and list of names should
# return "no duplicates".

fruits = ["apple", "orange", "banana", "apple"]
names = ["Yoda", "Moses", "Joshua", "Mark"]

for i in fruits:
    b = fruits.count(i)
if b > 1:
    print(f"{i} is duplicate value.")
else:
    print("No duplicate values.")


for i in names:
    c = names.count(i)
if c == 1:
    print(f"No duplicate values.")
else:
    print(f"{i} is duplicate value.")
