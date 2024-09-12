# Task 1
# Write a function called user_name that generates a username
# from the user’s email. The code should ask the user to input an
# email and the code should return everything before the @ sign
# as their user name. For example, if someone enters
# ben@gmail.com, the code should return ben as their user
# name.

a = input("Enter your email id: ")

if a[-10:] == '@gmail.com' or a[-12:] == '@outlook.com':
    print(f"Your username is: {a[:-10]}")

# Task 2
# Write a function called zeroed code that takes a list of numbers
# as an argument. The code should zero (0) the first and the last
# number in the list.

a = [2, 5, 7, 8, 9]

a.insert(0,0)
a.pop(1)
a.append(0)
a.pop(-2)
print(a)


