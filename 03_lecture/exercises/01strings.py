# """
# Write a program which asks the user for a string and an amount.
# The program then prints out the string as many times as specified by the amount.
# The printout should all be on one line, with no extra spaces or symbols added.
#
# Example:
#     Please type in a string: >> hey
#     Please type in an amount: >> 4
#     heyheyheyhey
# """
# # Write your solution here
#
# text = input("type in a string:")
# amount = int(input("amount:"))
# print(text * amount)
#
# """
# Write a program which asks the user for two strings and then prints out whichever is the longer of the two -
# that is, whichever has the more characters. If the strings are of equal length, the program
# should print out "The strings are equally long".
#
# Examples:
#
#     Please type in string 1: >> hello
#     Please type in string 2: >> world
#     The strings are equally long
#
#     Please type in string 1: >> hey
#     Please type in string 2: >> world
#     world is longer
# """
#
# # Write your solution here
# a_length = len(input("type in string 1:"))
# b_length = len(input("type in string 2:"))
#
# if a_length > b_length:
#     print(f"{a_length} is longer")
# elif b_length > a_length:
#     print(f"{b_length} is longer")
# else:
#     print("the strings are equally long")
#
#
# """
# Write a program which asks the user for a string. The program then prints out the input string in reversed order,
# from end to beginning. Each character should be on a separate line.
# Try to solve this example in 2 ways:
#     * once using positive indeces
#     * once using negative indeces
# """
# # Write your solution here
# str = input("String here: ")
# for i in range(-1, -len(str) - 1, -1): # start, until, step size
#     print(str[i])
#
# for i in range(len(str) - 1, -1, -1):
#     print(str[i])
#
# """
# Write a program which asks the user for a string.
# The program then prints out a message based on whether the second character and the second to last character
# are the same or not. See the examples below.
#
# Examples:
#     Please type in a string: >> python
#     The second and the second to last characters are different
#
#     Please type in a string: >> pascal
#     The second and the second to last characters are equal
# """
# # Write your solution here
# word = input("type in a string:")
#
# print(word[len(word)-2])    # get character at position length of the word minus 2. we start with index 0.
# result = "the second and the second to last characters are equal" if word[1] == word[len(word)-2] else "the second and the second to last characters are different"
# print(result)
#
# ## or using if else normal way
#
# if word[1] == word[len(word)-2]:
#     print("the second and the second to last characters are equal")
# else:
#     print("the second and the second to last characters are different")
#
# """
# Write a program which prints out a line of hash characters, the width of which is chosen by the user.
#
# Examples:
#     Width: >> 8
#     ########
#
#     Width: >> 2
#     ##
# """
# # Write your solution here

# width = input("width:")
# print("#" * int(width))
#
# """
# Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.
#
# Example:
#     Width: >> 10
#     Height: >> 3
#     ##########
#     ##########
#     ##########
# """
# # Write your solution here
#
# width = int(input("width:"))
# height = int(input("height:"))
# character = "#"
#
# #using nested for loops
# for i in range(0, height):
#     for j in range(0, width):
#         print(character, end="")
#     print()
#
# print("or using one loop only:")
#
# # using only one loop
# for el in range(0, height):
#     print(character * width)
#
# """
# Write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed.
# If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.
#
# You may assume the input string is at most 20 characters long.
#
# Examples:
#     Please type in a string:hello
#     ***************hello
#
#     Please type in a string:helloworld
#     **********helloworld
# """
# # Write your solution here
# user_input = input("type in a string:")
#
# print("*" * (20 - len(user_input)) + user_input)
#
# """
# Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre.
# The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.
#
# If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.
#
# Examples:
#     Word: >> testing
#
#     ******************************
#     *          testing           *
#     ******************************
#
#     Word: >> python
#
#     ******************************
#     *           python           *
#     ******************************
# """
# # Write your solution here
# frame_width = 30
# user_input = input("Word:")
# white_spaces = int((frame_width - 2 - len(user_input) )/2) # -2 for stars left and right, - length of word/2 (left and right side)
#
# print("*" * frame_width) # first line
# print("*" + white_spaces * " " + user_input + white_spaces * " " + "*")
# print("*" * frame_width) # last line
#
#
#
# """
# Write a program which asks the user to type in a string.
# The program then prints out all the substrings which begin with the first character,
# from the shortest to the longest. Have a look at the example below.
#
# Example:
#     Please type in a string: >> test
#     t
#     te
#     tes
#     test
# """
# # Write your solution here
# word = input("type in a string:")
#
# for c in range(1, len(word)):
#     print(word[0:c + 1])
#
#
# """
# Write a program which asks the user to input a string. The program then prints out different messages if the string
# contains any of the vowels a, e or o.
#
# You may assume the input will be in lowercase entirely. Have a look at the examples below.
#
#     Please type in a string: >> hello there
#     a not found
#     e found
#     o found
#
#     Please type in a string: >> hiya
#     a found
#     e not found
#     o not found
# """
# # Write your solution here
#
# text = input("type in a string:")
# vowels = "aeiou"
#
# for v in vowels:
#     result = f"{v} found" if v in text else f"{v} not found"
#     print(result)
#
#
# """
# Write a program which asks the user to type in a string and a single character. The program then
# prints the first three character slice which begins with the character specified by the user.
# You may assume the input string is at least three characters long. The program must print out three characters,
# or else nothing.
#
# Pay special attention to when there are less than two characters left in the string after the first occurrence of
# the character looked for. In that case nothing should be printed out, and there should not be any indexing errors
# when executing the program.
#
# Examples:
#
#     Please type in a word: >> mammoth
#     Please type in a character: >> m
#     mam
#
#     Please type in a word: >> banana
#     Please type in a character: >> n
#     nan
#
#     Please type in a word: >> python
#     Please type in a character: >> n
# """
# # Write your solution here
# word = input("type in a word:")
# character = input("type in a character:")
#
# start = word.find(character) # get index of character
#
# if start >= 0:
#     if start + 3 < len(word):
#         print(word[start:start+3])
#     else:
#         print("word not long enough to print 3")
# else:
#     print("character does not exist in word")

"""
Write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, 
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the 
substring aa is at index 2.

Examples:

    Please type in a string: >> abcabc
    Please type in a substring: >> ab
    The second occurrence of the substring is at index 3.
    
    Please type in a string: >> methodology
    Please type in a substring: >> o
    The second occurrence of the substring is at index 6.
    
    Please type in a string: >> aybabtu
    Please type in a substring: >> ba
    The substring does not occur twice in the string.
"""
# Write your solution here

word = input("type in a word:")
substring = input("type in a substring:")

first = word.find(substring)

if first >= 0:
    what_is_left = word[first + len(substring):len(word)] # get the right substring without first sub
    second = what_is_left.find(substring) # get index of what is left from the word
    if second >= 0:
        index = second + first + len(substring) # recalculate the index based on whole word
        print(f"the second occurrence of the substring is at index {index}")
    else:
        print("no second substring")
else:
    print("substring not found")