# Task 1
# Create a function called my_discount. The function takes no
# arguments but asks the user to input the price and the
# discount (percentage) of the product. Once the user inputs the
# price and discount, it calculates the price after the discount.
# The function should return the price after the discount. For
# example, if the user enters 150 as price and 15% as the discount,
# your function should return 127.5.

a = float(input("Enter your price: "))
b = float(input("Enter your discount: "))

c =  a - ((a*b)/100)

print(f"""
Price   =   {a}
Dicount =   {b}%
--------------------
Total   =   {c}
""")

# Task 2
# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school. The school
# has saved the students in a list. Your task is to write a code that
# will count how many males and females are in the list.
students = ['Male', 'Female', 'female', 'male', 'male', 'male',
'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
_male = []
_female = []

for i in students:
    if i == "male" or i == "Male":
        _male.append(i)   
    elif i == "female" or i == "Female":
        _female.append(i)


print(f"[('Male',{len(_male)}),('female',{len(_female)})]")