def main():
    num_of_words((get_book_text("books/frankenstein.txt")))

    # print(f"{num_words} words found in the document")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)


def num_of_words(string):
    list = string.split()
    print(list)


main()
