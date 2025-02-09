"""
Using only if statements for program flow leads to multiple executions of condition evaluation
"""
number = int(input("Please type in a number: "))

if number < 0:  # this expression is evaluated on each execution
    print("The number is negative")

if number >= 0: # this expression is evaluated on each execution
    print("The number is positive or zero")

"""
Instead of creating a whole another conditional statement, as in the example above, 
it is possible to create another branch of the same conditional statement to cover 
all cases where the condition was false. This is called the else statement.
"""

number = int(input("Please type in a number: "))

if number < 0:   # this expression is evaluated on each execution
    print("The number is negative")
else:           # this expression is only reached when if statement resolve to false
    print("The number is positive or zero")


"""
String comparison
"""
correct = "kittycat"
password = input("Please type in the password: ")

if password == correct:
    print("Welcome")
else:
    print("No admittance")


"""
Elif Statement
"""
print("Holiday calendar")
date = input("What is the date today? ")

if date == "Dec 26":
    print("It's Boxing Day")
elif date == "Dec 31":
    print("It's Hogmanay")
elif date == "Jan 1":
    print("It's New Year's Day")

print("Thanks and bye.")

"""
Combining conditions
"""

number = int(input("Please type in a number: "))
if number >= 5 and number <= 8:
    print("The number is between 5 and 8")

number = int(input("Please type in a number: "))
if number < 5 or number > 8:
    print("The number is not within the range of 5 to 8")

n1 = int(input("Number 1: "))
n2 = int(input("Number 2: "))
n3 = int(input("Number 3: "))
n4 = int(input("Number 4: "))

if n1 > n2 and n1 > n3 and n1 > n4:
    greatest = n1
elif n2 > n3 and n2 > n4:
    greatest = n2
elif n3 > n4:
    greatest = n3
else:
    greatest = n4

print(f" {greatest} is the greatest of the numbers.")

"""
Nesting Conditions
"""

number = int(input("Please type in a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
else:
    print("The number is negative or zero")
