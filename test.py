'''
Grade Calculator (if, elif, else)

Take percentage as input from the user and print the grade according to:
Percentage ≥ 80 → Grade A+
Percentage ≥ 70 → Grade A
Percentage ≥ 60 → Grade B
Percentage ≥ 50 → Grade C
Otherwise → Fail
'''
def grade_calculator():
    marks = int(input("Enter Your Marks: "))
    if marks >= 80:
        print("Grade A+")
    elif marks >= 70:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    elif marks >= 50:
        print("Grade C")
    else:
        print("Fail")
grade_calculator()

'''
Palindrome Number

Take a number as input and check whether it is a palindrome or not.
'''
def check_palindrome():
    num = int(input("Enter a number: "))
    copy = num
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    if copy == rev:
        print(f"{copy} is a palindrome number.")
    else:
        print(f"{copy} is not a palindrome number.")
check_palindrome()

'''
Factorial of a Number

Take a number as input and find its factorial.
'''
def factorial():
    num = int(input("Enter a number: "))
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"The factorial of {num} is {fact}.")
factorial()

'''
Count Even and Odd Numbers in a Range

Take starting number and ending number from the user.
Count how many even and odd numbers are present in that range.
'''
def count_even_odd_bw_range():
    start = int(input("Enter Your Starting Number: "))
    end = int(input("Enter Your Ending Number: "))
    even_count = 0
    odd_count = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(f"Total Even Numbers: {even_count}")
    print(f"Total Odd Numbers: {odd_count}")
count_even_odd_bw_range()

'''
Number Divisible by 3 and 5

Take a range from the user and print all numbers that are divisible by both 3 and 5.
'''
def divisible_by_3_and_5():
    start = int(input("Enter Your Starting Number: "))
    end = int(input("Enter Your Ending Number: "))
    for i in range(start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
        print("Numbers divisible by both 3 and 5 in the given range are printed above.")
divisible_by_3_and_5()
