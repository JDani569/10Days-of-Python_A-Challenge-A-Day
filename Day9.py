# Task 1
# Create a function called biggest_odd that takes a string of
# numbers and returns the biggest odd number in the list. For
# example, if you pass ‘23569’ as an argument, your function
# should return 9. Use list comprehension.

a = int(input("enter your range: "))

# method 1
b = [i for i in range(0,a) if i % 2 == 1 ]
print(b[-1])

# # method 2
c = []
for i in range(0,a):
    if i % 2 == 1:
        b.append(i)
        c.sort()
print("Your list is: ",c)
print(c[-1])


# Task 2
# Write a function called zeros_last. This function takes a list as
# argument. If a list has zeros (0), it will move them to the front of
# the list and maintain the order of the other numbers in the list.
# If there are no Zeros in the list, the function should return the
# original list sorted in ascending order. For example, if you pass
# [1, 4, 6, 0, 7,0,9] as an argument, your code should return [1,
# 4, 6, 7, 9, 0, 0]. If you pass [2, 1, 4, 7, 6] as your argument,
# your code should return [1, 2, 4, 6, 7].

a = [2, 1, 4, 7, 6]

if 0 not in a:
    a.sort()
    print(f"Your sorted list is: {a}")
else:
    for i in a:
        if i == 0:
            a.pop(a.index(i))
            a.append(0)
    print(f"Your sorted list is: {a}")