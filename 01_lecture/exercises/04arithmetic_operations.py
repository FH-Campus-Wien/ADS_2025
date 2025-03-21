"""
Write a program which asks the user for a number.
The program then prints out the number multiplied by five.
Example:
    Please type in a number: >> 7
    7 times 5 is 35
"""
# Write your solution here

number = int(input("type in a number:"))    # casting necessary to multiply afterwards
print(f"{number} times 5 is {(number*5)}")

"""
Write a program which asks the user for their name and year of birth.
The program then prints out a message as follows:
    What is your name? >> Frances Fictitious
    Which year were you born? >> 1990
    Hi Frances Fictitious, you will be 34 years old at the end of the year 2024
"""
# Write your solution here
name = input("your name?")
born = int(input("born?"))

print(f"Hi {name}, you will be {2024 - born} years old at the end of the year 2024")

"""
Write a program which asks the user for a number of days.
The program then prints out the number of seconds in the amount of days given.
Example:
    How many days? >> 7
    Seconds in that many days: 604800
"""
# Write your solution here

days = int(input("How many days?"))
print(f"Seconds in that many days: {days * 24 * 60 * 60}")

"""
This program asks the user for three numbers.
The program then prints out their product, that is, the numbers multiplied by each other.
There is, however, something wrong with the program - it doesn't work quite right, as you can see if you run it.
Please fix it.
"""
# Fix the code
number = int(input("Please type in the first number: "))
number2 = int(input("Please type in the second number: "))
number3 = int(input("Please type in the third number: "))

product = number * number2 * number3

print("The product is", product)


"""
Write a program which asks the user for four numbers.
The program then prints out the sum and the mean of the numbers.
Example:
    Number 1: >> 2
    Number 2: >> 1
    Number 3: >> 6
    Number 4: >> 7
    The sum of the numbers is 16 and the mean is 4.0
"""
# Write your solution here
n1 = int(input("number 1:"))
n2 = int(input("number 2:"))
n3 = int(input("number 3:"))
n4 = int(input("number 4:"))

print(f"The sum of the numbers is {n1 + n2 + n3 + n4} and the mean is {(n1 + n2 + n3 + n4)/4}")

"""
Write a program that asks the user for a three-digit number input.
Reverse the given number by using modulo and division operator.
Example:
    Enter a number: >> 123
    The reversed number is: 321
"""
# Write your solution here

n5 = int(input("enter a number:"))

first = n5%10
second = int(n5/10%10) # 123/10 -> 12,3; 12,3%10 -> 2,3000007 -> int() will remove the decimal
third = int(n5/100) # cast to int to remove decimal


print(f"The reversed number is: {first}{second}{third}")
