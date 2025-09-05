from stats import get_num_words, words_frequency, sort_dictionary

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print("============ BOOKBOT ============")
    file_string = get_book_text("books/frankenstein.txt")
    print("Analyzing book found at books/frankenstein.txt...")
    num_words = get_num_words(file_string)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_dictionary_sorted = sort_dictionary(words_frequency(file_string))
    for d in list_dictionary_sorted:
        ch, val = d.items()
        print(f"{ch[1]}: {val[1]}")
    print("============= END ===============")

main()
