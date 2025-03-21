"""
Write a program that asks for a user's name and then prints it twice

    What is your name? >> Leon
    Leon
    Leon
"""
# Write your solution here

name = input("what is your name?")
print(name)
print(name)
# or
print((name + "\n") * 2)

"""
 Write a program that asks for a user's name and then prints it out twice separated by exclamation marks

    What is your name? >> Leon
    !Leon!Leon!
"""
# Write your solution here

name2 = input("whats your name?")
# using f string
print(f"!{name2}!{name2}!")
# using concatination
print("!" + name2 + "!" + name2 + "!")


"""
Here is a program which should ask for three utterances and print them out, like so:

    The 1st part: >> hickory
    The 2nd part: >> dickory
    The 3rd part: >> dock
    hickory-dickory-dock!
"""

# Fix the code
part = input("The 1st part: ")
part2 = input("The 2nd part: ")
part3 = input("The 3rd part: ")
print(f"{part}-{part2}-{part3}!")

"""
Write a program which prints out the following story. The user gives a name and a year, which should be inserted into the printout.

    Please type in a name: >> Mary
    Please type in a year: >> 1572
    
    Mary is a valiant knight, born in the year 1572. One morning Mary woke up to an awful racket: a dragon was approaching the village. Only Mary could save the village's residents.
"""
# Write your solution here
story_name = input("type in a name: ")
year = input("type in a year: ")

print(f"{story_name} is a valiant knight, born in the year {year}. One morning {story_name} woke up to an awful racket: a dragon was approaching the village. Only {story_name} could save the village's residents.")