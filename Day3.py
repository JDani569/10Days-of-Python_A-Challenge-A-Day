# Task 1
# Write a function called register_check that checks how many
# students are in school. The function takes a dictionary as a
# parameter. If the student is in school, the dictionary says ‘yes’. If
# the student is not in school, the dictionary says ‘no’. Your
# function should return the number of students in school. Use the
# dictionary below. Your function should return 3.
register = {'Michael':'yes',
            'John': 'no',
            'Peter':'yes', 
            'Mary': 'yes'}
a = list(register.values())
c = 0
d = 0

for i in set(a):
    if i == 'yes':
        c += a.count(i)
    else:
        d += a.count(i)
print(f"Registered: {c}")
print(f"Un-egistered: {d}")

# Task 2
# You are given a list of names above. This list is made up of names
# of lowercase and uppercase letters. Your task is to write a code
# that will return a tuple of all the names in the list that have only
# lowercase letters. Your tuple should have names sorted
# alphabetically in descending order.
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
a = []

for i in names:
    if i.islower():
        a.append(i)
        a.sort(reverse=True)
print(tuple(a))


