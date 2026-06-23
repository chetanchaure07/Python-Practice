'''
Sum of Even Numbers

Print the sum of all even numbers from 1 to 100 using a for loop.
'''
sum = 0
for i in range(0, 101, 2):
    sum += i
print("The sum of all even numbers from 1 to 100 is:", sum)

'''
Multiplication Table

Generate the multiplication table of a given number n up to 20.
'''
n = int(input("Enter a number to generate its multiplication table: "))
for i in range(1, 21):
    print(f"{n} x {i} = {n * i}")

'''
Count Digits

Given a number, count how many digits it contains using a loop.
'''
number = int(input("Enter a number: "))
count = 0
for i in str(number):
    count += 1
print(f"The number {number} contains {count} digits.")

'''
Reverse a String

Reverse a string without using built-in reverse functions.
'''
string = input("Enter a string to reverse: ")
rev_str = ""
for i in string:
    rev_str = i + rev_str
print(f"The reversed string is: {rev_str}")

'''
Find Prime Numbers

Print all prime numbers between 1 and 100.
'''
print("Prime numbers between 1 and 100 are:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num // 2) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

'''
Frequency Counter

Count the occurrence of each character in a string.
'''
string = input("Enter a string to count character frequency: ")
frequency = {}
for char in string:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(frequency)

'''
Pattern Printing

Print:

*
**
***
****
*****
'''
for i in range(1, 6):
    print("*" * i)

'''
Fibonacci Series

Print the first n Fibonacci numbers using a loop.
'''
n = int(input("Enter the number of Fibonacci numbers to print: "))
a = 0
b = 1
for i in range(1, n + 1):
    print(a)
    c = b + a
    a = b
    b = c

'''
Armstrong Numbers

Find all Armstrong numbers between 1 and 1000.
'''
print("Armstrong numbers between 1 and 1000 are:")

for num in range(1, 1001):
    copy = num
    power = len(str(num))
    total = 0

    while num > 0:
        digit = num % 10
        total += digit ** power
        num //= 10

    if copy == total:
        print(copy)

'''
Perfect Numbers

Print all perfect numbers between 1 and 10000.
'''
print("Perfect numbers between 1 and 10000 are:")
for num in range(1, 10001):
    sum = 0
    for i in range(1, (num // 2) + 1):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num)

