from stats import num_of_words, num_char, sort_list
import sys

if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(path):
    with open (f"{path}") as frankenstein:
        book_contents = frankenstein.read()
    return book_contents

def pretty_print (num_words, sorted_list):
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}")
    print ("----------- Word Count ----------")
    print (f"Found {num_words} total words")
    print ("--------- Character Count -------")
    for d in sorted_list:
        for char, count in d.items():
            print(f"{char}: {count}")
    print ("============= END ===============")

def main():
    book = get_book_text(sys.argv[1])
    num_words = num_of_words(book)
    num_chars = num_char(book)
    sorted_list = sort_list(num_chars)

    return pretty_print(num_words, sorted_list)

print (main())

print (sys.argv)