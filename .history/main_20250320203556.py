from stats import num_of_words


def main():
    num_words = num_of_words((get_book_text("books/frankenstein.txt")))

    print(f"{num_words} words found in the document")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)


main()
