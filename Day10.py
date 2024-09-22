# Task 1
# Write a function called hide_password that takes no
# parameters. The function takes an input (a password) from a
# user and returns a hidden password. For example, if the user
# enters ‘hello’ as a password the function should return ‘****’ as
# a password and tell the user that the password is 4 characters
# long.

password = input("Enter your password: ")
a = ''
for i in password:
    a += '*'
print(f"Your password is {a} and {len(password)} characters long.")

# Task 2
a = [1000000, 2356989, 2354672, 9878098]
b = []

for i in a:
    c = "{:,}".format(i)
    b.append(c)
print(b)
        

