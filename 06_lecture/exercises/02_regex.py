import re

"""
Using a regular expression, please write a function named is_dotw(my_string: str).
The function should return True if the string passed as an argument contains an abbreviation
for a day of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun).

Examples:
    print(is_dotw("Mon")) # True
    print(is_dotw("Fri")) # True
    print(is_dotw("Tui")) # False
"""
def is_dotw(my_string: str):
    pattern = r'^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)$'
    return bool(re.search(pattern, my_string))

# Examples
print(is_dotw("Mon"))  # True
print(is_dotw("Fri"))  # True
print(is_dotw("Tui"))  # False
print(is_dotw("Today is Wednesday"))  # True
print(is_dotw("Tomorrow is Thrs"))  # False


"""
Write a function named all_vowels(my_string: str) which uses a regular expression to check whether all characters in the given string are vowels.

Some examples of how the function should work:

    print(all_vowels("eioueioieoieou")) # True
    print(all_vowels("autoooo"))        # False
"""
def all_vowels(my_string: str):
    pattern = r'^[aeiouAEIOU]+$'
    return bool(re.search(pattern, my_string))

# Examples
print("vowels:")
print(all_vowels("eioueioieoieou"))  # True
print(all_vowels("autoooo"))         # False
print(all_vowels("AEIOU"))           # True
print(all_vowels("aEiOu"))           # True
print(all_vowels("hello"))           # False

"""
Write a function named time_of_day(my_string: str) which uses a regular expression to check whether 
a string in the format XX:YY:ZZ is a valid time in the 24-hour format, with two digits each for 
hours, minutes and seconds.

Some examples of how the function should work:
    print(time_of_day("12:43:01"))  # True
    print(time_of_day("AB:01:CD"))  # False
    print(time_of_day("17:59:59"))  # True
    print(time_of_day("33:66:77"))  # False
"""
def time_of_day(my_string: str):
    # regular expression pattern for matching valid 24-hour time format
    pattern = r'^(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])$'
    return bool(re.search(pattern, my_string))

# Examples
print(time_of_day("12:43:01"))  # True
print(time_of_day("AB:01:CD"))  # False
print(time_of_day("17:59:59"))  # True
print(time_of_day("33:66:77"))  # False