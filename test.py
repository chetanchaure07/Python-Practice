# Factorial Using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
factorial(5)


# Prime No between range
def prime():
    start = int(input("Enter starting value: "))
    end = int(input("Enter ending value: "))
    for i in range(start , end + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:

            print(f"{i} is a prime no")
        else:
            print(f"{i} is not a prime no")
prime()

# Count Vowel in sting
def vowel_count():
    string = input("Enter Your String: ").lower()
    vowel = "aeiou"
    count = 0
    for i in string:
        if i in vowel:
            count += 1
    print(f"{string} has {count} no of vowel.")

vowel_count()

# Armstrong Number Using Function
def armstrong():
    num = int(input("Enter Your number: "))
    copy = num
    sum = 0
    fact = len(str(num))
    while num > 0:
        last = num % 10
        sum += last ** fact
        num //= 10
    if copy == sum:
        print(f"{copy} is armstrong number.")
    else:
        print(f"{copy} is not an armstrong number.")

armstrong()

# Sum of Digits Using Function
def sum_of_digit():
    num = int(input("Enter your number: "))
    copy = num
    sum = 0
    while num > 0:
        last = num % 10
        sum += last
        num //= 10
    print(f"{copy} number sum is : {sum}")

sum_of_digit()