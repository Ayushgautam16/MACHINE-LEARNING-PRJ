# questio 1

numbers = [1, -2, 3, -4, 5, 6, -7, 8, 9, 10]

positive_numbers = 0
for num in numbers:
    if num > 0:
        positive_numbers += 1

print ("Number of positive numbers:", positive_numbers)
   
# question 2
numbers =10
sum_even = 0
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))
numbers = int(input("enter the number you want to enter: "))

for i in range(1,n+1):
    if i%2 == 0:
        sum_even += 1
    
print("sum of even numbers:", sum_even)

#  question 3

number =3
for i in range(1,11):
    if i == 5:
        continue
    print(number,"x",i,"=",number*i)

# skip the 5th iteration

# question 4

input_str ="Python"
reversed_str = ""

for char in input_str:
    reversed_str = char + reversed_str

print("Reversed string:", reversed_str)

# question 5
# first non repeated char

input_str = "teetermined"

for char in input_str:
    if input_str.count(char) == 1:
        print(char)
        break

# quetion 6

number = 9
factorial =1

while number > 0:
    factorial = factorial* number
    number -= 1

print("Factorial of number", "is:", factorial)

# question 6
while True:
    number = int(input("enter the num b/w 1 and 10: "))
    if 1 <= number <= 10:
        print("thanks")
        break
    else:
        print("invalid number")

# question 7

number = 42

is_prime = True

if number >1:
    for i in range (2,number):
        if(number %i) == 0:
            is_prime = False
            break

print(is_prime)

# question 8
items = ["apple", "banana", "strawberry", "grapes", "orange", "apple"]

unique_items =set()

for item in items:
    if item in unique_items:
        print("duplicate :",item )
        break
    unique_items.add(item)

# question 9

import time 

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("attempts ", attempts, +1 , "wait time ", wait_time)
    wait_time *= 2
    attempts *= 1