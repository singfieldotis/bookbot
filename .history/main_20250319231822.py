def main():
    print(get_book_text("books/frankenstein.txt"))


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return str(file_contents)


def num_of_words(string):


main()
