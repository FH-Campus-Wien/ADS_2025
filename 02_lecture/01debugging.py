"""
Short Debugging Demo
"""

number_of_characters = len(input("Enter a word:"))  # the len function can be used to find out the length of a string

print("Your word has " + str(number_of_characters) + " characters.")

if number_of_characters < 1:
    print("No empty input allowed...")
elif number_of_characters < 4:
    print("Very short word you chose..")
elif number_of_characters < 10:
    print("Looks like a normal length for words")
else:
    print("Very long word.")

print("After if/else branch")


## More typecasting
temperature = float(input("Please type in a temperature: "))

print("The temperature is", temperature)

print("...and rounded down it is", int(temperature))