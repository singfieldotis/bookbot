from stats import num_of_words
from stats import letter_counter
import sys

booktext = ""


def main():
    num_words = num_of_words((get_book_text(booktext)))

    count_of_letters = letter_counter(get_book_text(booktext))

    print(f"{num_words} words found in the document")

    print(count_of_letters)


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)


main()
