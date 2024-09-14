# Task 1
# Write a function called odd_even that has one parameter and
# takes a list of numbers as an argument. The function returns the
# difference between the largest even number in the list and the
# smallest odd number in the list. For example, if you pass
# [1,2,4,6] as an argument the function should return 6 -1= 5.

a = int(input("Enter your staring range: "))
b = int(input("Enter your ending range: "))
d = []

for i in range(a,b):
    d.append(i)
    d.sort()
    if d[-1] % 2 == 0:
        c = d[-1] - d[0]
    
print("Your list is: ",d)
print(c)   

# Task 2
# Write a function called prime_numbers. This function asks a
# user to enter a number (integer) as an argument and returns a
# list of all the prime numbers within its range. For example, if user
# enters 10, your code should return [2, 3, 5, 7] as prime numbers.
a1 = int(input("Enter your range: "))
b = []
if a1 >1:
    for i in range(2,int(a1/2)):
        if (a1 % i) == 0:
            b.append(i) 
    print(b)
  
