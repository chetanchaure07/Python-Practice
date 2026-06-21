'''
Factorial Using While Loop

Take a number n from the user and find its factorial using a while loop.
'''
from random import random


def factorial_while():
    num = int(input("Enter a number: "))
    fact = 1
    i = 1
    while i <= num:
        fact *= i
        i += 1
    print(f"The factorial of {num} is {fact}.")
factorial_while()

'''
Fibonacci Series

Print the first n terms of the Fibonacci sequence using a while loop.
'''
def fibonacci():
    n = int(input("Enter the number of terms: "))
    a = 0
    b = 1
    count = 0

    while count < n:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        count += 1
fibonacci()

'''
Sum of Digits

Take a number from the user and find the sum of its digits using a while loop.
'''
def sum_of_digits():
    num = int(input("Enter a number: "))
    copy = num
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num = num // 10
    print(f"Sum of {copy} is: {total}")
sum_of_digits()

'''
Product of Digits

Take a number from the user and find the product of its digits using a while loop.
'''
def product_of_digits():
    num = int(input("Enter a number: "))
    copy = num
    product = 1
    while num > 0:
        digit = num % 10
        product *= digit
        num = num // 10
    print(f"Product of {copy} is: {product}")
product_of_digits()

'''
Check Palindrome Number

Take a number from the user and check whether it is a palindrome using a while loop.
'''
def palindrome_number():
    num = int(input("Enter a number: "))
    copy = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10
    if copy == reverse:
        print(f"{copy} is a palindrome number.")
    else:
        print(f"{copy} is not a palindrome number.")
palindrome_number()

'''
Check Armstrong Number

Take a number from the user and determine whether it is an Armstrong number.
'''
def armstrong_number():
    num = int(input("Enter a number: "))
    copy = num
    power = len(str(num))
    sum = 0 
    while num > 0:
        digit = num % 10
        sum += digit ** power
        num = num // 10
    if copy == sum:
        print(f"{copy} is an Armstrong number.")
    else:
        print(f"{copy} is not an Armstrong number.")
armstrong_number()

'''
Find Greatest Common Divisor (GCD)

Take two numbers from the user and find their GCD using the Euclidean algorithm with a while loop.
'''
def gcd():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number:"))
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    print(f"The GCD is: {a}")
gcd()

'''
Count Frequency of a Digit

Take a number and a digit from the user. Count how many times the digit appears in the number.
'''
def count_frequency():
    num = int(input("Enter a number: "))
    digit = int(input("Enter a digit to count its frequency: "))
    count = 0 
    while num > 0:
        last = num % 10
        if last == digit:
            count += 1
        num = num // 10
    print(f"The digit {digit} appears {count} times in the number.")
count_frequency()

'''
Decimal to Binary Conversion

Convert a decimal number into binary using only a while loop.
'''
def decimal_to_binary():
    num = int(input("Enter a decimal number: "))
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    print(f"The binary representation is: {binary}")
decimal_to_binary()

'''
Decimal to Octal Conversion

Convert a decimal number into octal using only a while loop.
'''
def decimal_to_octal():
    num = int(input("Enter a decimal number: "))
    octal = ""
    while num > 0:
        octal = str(num % 8) + octal
        num = num // 8
    print(f"The octal representation is: {octal}")
decimal_to_octal()

'''
Binary to Decimal Conversion

Convert a binary number into decimal using only a while loop.
'''
def binary_to_decimal():
    num = input("Enter a binary number: ")
    decimal = 0
    power = 0
    i = len(num) - 1
    while i >= 0:
        decimal += int(num[i]) * (2 ** power)
        power += 1
        i -= 1
    print(f"The decimal representation is: {decimal}")
binary_to_decimal()

'''
Reverse Words in a String (Without Built-in Reverse)

Take a sentence and reverse each word using while loops.
'''
def reverse_words():
    word = input("Enter your string: ")
    rev = ""
    i = 0
    while i < len(word):
        rev = word[i] + rev
        i += 1
    print(f"Your reveresed word is: {rev}")
reverse_words()

'''
Prime Number Check

Check whether a given number is prime using a while loop.
'''
def prime_no():
    num = int(input("Enter your number: "))
    is_prime = False
    if num > 1:
        is_prime = True
        i = 2
        while i <= num // 2:
            if num % i == 0:
                is_prime = False
                break
            i += 1
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
prime_no()

'''
Print All Prime Numbers in a Range

Take two numbers and print all prime numbers between them using nested while loops.
'''
def prime_range():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))
    print(f"Prime numbers between {start} and {end} are:")
    while start <= end:
        is_prime = True
        if start > 1:
            i = 2
            while i <= start // 2:
                if start % i == 0:
                    is_prime = False
                    break
                i += 1
            if is_prime:
                print(start, end=" ")
        start += 1
prime_range()

'''
Find LCM of Two Numbers

Find the Least Common Multiple of two numbers using a while loop.
'''
def lcm():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    max_num = max(a, b)
    lcm_value = max_num
    while True:
        if lcm_value % a == 0 and lcm_value % b == 0:
            break
        lcm_value += max_num
    print(f"The LCM of {a} and {b} is: {lcm_value}")
lcm()

'''
Number Guessing Game

Generate a secret number and keep asking the user to guess until they get it right.
'''
import random
def number_guessing_game():
    secret_number = random.randint(1, 100)
    guess = None
    while guess != secret_number:
        guess = int(input("Guess the number (between 1 and 100): "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
    print("Congratulations! You guessed the number correctly.")