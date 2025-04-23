def num_of_words(string):
    list = string.split()
    return len(list)


def letter_counter(string):
    string = string.lower()

    letter_counts: dict[str, int] = {}

    for char in string:
        letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts
