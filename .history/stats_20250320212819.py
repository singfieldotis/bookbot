def num_of_words(string):
    list = string.split()
    return len(list)


def letter_counter(string):
    string = string.lower()

    letter_counts: dict[str, int] = {}

    for char in string:
        counts[char] = counts.get(char, 0) + 1
