from stats import get_num_words, words_frequency, sort_dictionary

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_string = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(file_string)
    print(f"{num_words} words found in the document")
    print(sort_dictionary(words_frequency(file_string)))

main()
