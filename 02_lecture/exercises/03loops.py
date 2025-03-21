"""
Write a program that prints out the message "hello world!" and then asks "shall we continue?"
until the user inputs "no". Then the program should print out "okay then" and finish.

Example:
    hello world!
    shall we continue? >> yes
    hello world!
    shall we continue? >> oui
    hello world!
    shall we continue? >> jawohl
    hello world!
    shall we continue? >> no
    okay then
"""
# Write your solution here

user_input = ""
while user_input != "no":
  print("hello world!")
  user_input = input("shall we continue?")

print("okay then")

"""
Write a program which asks the user for integer numbers.

- If the number is below zero, the program should print out the message "invalid number".
- If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
- In either case, the program should then ask for another number.
- If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

To use the `sqrt` function in python add the following to the top of your file: 
    from math import sqrt
Then use it like:
    print(sqrt(9))
    
Example:
    Please type in a number: >> 16
    4.0
    Please type in a number: >> 4
    2.0
    Please type in a number: >> -3
    invalid number
    Please type in a number: >> 1
    1.0
    Please type in a number: >> 0
    Exiting...
"""
# Write your solution here

"""
This program should print out a countdown. However, the program doesn't quite work. Please fix it.
Hint: you can use the debugger of PyCharm to see how the program is executing.
"""
# Fix the code
number = 5
print("Countdown!")
while number >= 0:
  print(number)
  number = number - 1

print("Now!")

"""
Write a program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.

Examples:
    Year: >> 2023
    The next leap year after 2023 is 2024
    
    Year: >> 2024
    The next leap year after 2024 is 2028
"""
# Write your solution here

year = int(input("Year: "))

while True:
  year += 1
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The next leap year after {year - 1} is {year}")
    break

### without using while True:
year = int(input("Year: "))

year += 1
while not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
  year += 1

print(f"The next leap year after {year - 1} is {year}")


"""
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.

Example:
  Please type in a word: >> Once
  Please type in a word: >> upon
  Please type in a word: >> a
  Please type in a word: >> time
  Please type in a word: >> there
  Please type in a word: >> was
  Please type in a word: >> a
  Please type in a word: >> girl
  Please type in a word: >> end
  Once upon a time there was a girl
"""
# Write your solution here

story = ""

while True:
  word = input("Please type in a word: ")
  if word == "end":
    break
  if story:
    story += " " + word
  else:
    story = word

print(story)

"""
Change the program above so that the loop ends also if the user types in the same word twice in a row.
"""
# Write your solution here

story = ""
prev_word = ""

while True:
  word = input("Please type in a word: ")
  if word == "end" or word == prev_word:
    break
  if story:
    story += " " + word
  else:
    story = word
  prev_word = word

print(story)

"""
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in 0.

After reading the numbers the program should 
  - print out how many numbers were typed in
  - the sum of numbers entered
  - the mean of numbers entered
  - the number of positive and negative numbers entered
  
Example output
  Numbers typed in 4
  The sum of the numbers is 34
  The mean of the numbers is 8.5
  Positive numbers 3
  Negative numbers 1
"""
# Write your solution here
# Initialize variables to store the sum, count, positive and negative counts
total_sum = 0
count = 0
positive_count = 0
negative_count = 0

# Keep asking for numbers until the user enters 0
number = int(input("Enter an integer (0 to stop): "))

while number != 0:
  total_sum += number
  count += 1

  # Check if the number is positive or negative and update the respective count
  if number > 0:
    positive_count += 1
  elif number < 0:
    negative_count += 1

  # Ask for the next number
  number = int(input("Enter an integer (0 to stop): "))

# After the loop, print the results
if count > 0:
  mean = total_sum / count
  print(f"\nNumbers typed in: {count}")
  print(f"The sum of the numbers is {total_sum}")
  print(f"The mean of the numbers is {mean}")
  print(f"Positive numbers: {positive_count}")
  print(f"Negative numbers: {negative_count}")
else:
  print("No numbers were entered.")

"""
Largest Number

Write a program which asks the user for float numbers.
The program should keep asking for numbers until the user types in 0 or a negative number.
The program should then print the largest number.
If the first number entered is less than or equals to 0, the program should quit and print "no number entered".

DO NOT USE LISTS TO SOLVE THIS EXERCISE!

Examples:
  Number 1: >> 3
  Number 2: >> 4.67
  Number 3: >> 120.5
  Number 4: >> 70
  Number 5: >> 0
  The largest number is 120.5
  
  Number 1: >> -1.11
  No number entered.
"""
# Write your solution here

"""
Write a program that reads in an integer number (number of lines) and generates the subsequent output using 
two loops on the console (see below). 
If the input of numbers is smaller or equal to 0 an error message should be printed.

Examples:
  n: >> 4
  1
  2 3
  4 5 6
  7 8 9 10
  
  n: >> -1
  Invalid number!
"""
# Write your solution here

count = 1
number = float(input(f"Number {count}: >> "))

if number <= 0:
    print("No number entered.")
else:
    largest_number = number
    count += 1

    # Ask for the next number
    number = float(input(f"Number {count}: >> "))

    while number > 0:
        # Update the largest number if the current number is larger
        if number > largest_number:
            largest_number = number
        count += 1
        number = float(input(f"Number {count}: >> "))

    # Print the largest number found
    print(f"The largest number is {largest_number}")


"""
Write a program that uses loops to create a pyramid of stars '*' on the console. 
The pyramid should have exactly 6 rows.
Example:
       *
      ***
     *****
    *******
   *********
  ***********
"""
# Write your solution here
# Number of rows in the pyramid
rows = 6

#### solution without nesting loops using a range
for i in range(1, rows + 1):
  # Print leading spaces
  print(' ' * (rows - i), end='')

  # Print stars
  print('*' * (2 * i - 1))


#### Using while loops
rows = 6
i = 1

while i <= rows:
  # print leading spaces
  j = 1
  while j <= (rows - i):
    print(' ', end='')
    j += 1

  # print stars
  k = 1
  while k <= (2 * i - 1):
    print('*', end='')
    k += 1

  # next line
  print()

  i += 1

"""
Write a program to calculate the average grade. The console reads in grades between 1 and 5 
until the number 0 is entered. If an invalid grade is entered, an error message is displayed, 
the grade is not counted and the prompt progresses. It is assumed that only integers are entered. 
At the end of the input, the grade average and the number of negatives (grade = 5) are output.

Example:
  Mark 1: >> 5
  Mark 2: >> 3
  Mark 3: >> 10
  Invalid mark!
  Mark 3: >> 1
  Mark 4: >> 5
  Mark 5: >> 0
  Average: 3.50
  Negative marks: 2
"""
# Write your solution here

total_sum = 0
count = 0
negative_count = 0

mark_number = 1
mark = int(input(f"Mark {mark_number}: >> "))

while mark != 0:
  # If the mark is valid (between 1 and 5)
  if 1 <= mark <= 5:
    total_sum += mark
    count += 1
    if mark == 5:
      negative_count += 1
  else:
    print("Invalid mark!")

  mark_number += 1
  mark = int(input(f"Mark {mark_number}: >> "))  # ask for the next mark

if count > 0:
  average = total_sum / count
  print(f"Average: {average:.2f}")
  print(f"Negative marks: {negative_count}")
else:
  print("No valid grades entered.")
