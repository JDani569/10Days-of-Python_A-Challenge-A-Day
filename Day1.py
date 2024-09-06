# Task 1
# Write a function called divide_or_square that takes one
# argument (a number), and returns the square root of the number
# if it is divisible by 5, returns its remainder if it is not divisible by
# 5. For example, if you pass 10 as an argument, then your function
# should return 3.16 as the square root.
a = int(input("Enter your number: "))

if a % 5 == 0:
    print(f"Sqrt of {a} is {a ** (1/2): .2f}")
elif a < 5:
    print("Enter number greater than 5.")
else:
    print(f"Remainder of {a} is {a%5}")

# Task 2
# Write a function called longest_value that takes a dictionary
# as an argument and returns the first longest value of the
# dictionary. For example, the following dictionary should return
# – apple as the longest value.

a = {'fruit':'banana',
     'color':'apple'}
b = list(a.values())
s = 0
s1 = 0

for i in b[0]:
    s += ord(i)
for i in b[1]:
    s1 += ord(i)

if s > s1:
    print(f"{b[0]} is largest.")
else:
    print(f"{b[1]} is largest.")