import re


def countWordOccurences():
    """
    Count the number of times each word appears inside the bee movie script
    and save each word with the amount of times it occurred in a dictionary
    Don't differentiate between capitalized and non-capitalized letters
    :return: A dictionary containing all words and the amount of times they occur
    """
    with open("Bee Movie Script.txt") as bee_script:
        bee_script = bee_script.read().lower()
        words = re.findall(r'\b\w+\b', bee_script)
        # Create a dictionary to hold word counts
        word_counts = {}

        # Count each word
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

        return word_counts


def largestCalories():
    """
    Inside the Calories.txt, multiple 'boxes' of calories are listed, each box
    being seperated by an empty line. In the Calories_small.txt you have an easier list to test with
    In the example, the first box would contain 1000, 2000 and 3000 calories, the second box
    contains only 4000 calories. In this example the largest box would be box 4 with
    a sum of 24000 calories. Find the largest box.
    :return: The amount of calories in the largest box
    """
    with open("Calories.txt") as calories:
        content = calories.read()

    # Split the content into separate boxes based on empty lines
    boxes = content.strip().split('\n\n')

    # Initialize variables to store the largest box and its sum of calories
    largest_box_sum = 0

    # Iterate through each box
    for box in boxes:
        # Calculate the sum of calories in the current box
        box_calories = 0
        # box_calories = sum(int(calories) for calories in box.split('\n'))
        for calories in box.split('\n'):
            box_calories += int(calories)

        # Update the largest box sum if necessary
        if box_calories > largest_box_sum:
            largest_box_sum = box_calories

    return largest_box_sum


if __name__ == "__main__":
    print(countWordOccurences())
    print(largestCalories())
