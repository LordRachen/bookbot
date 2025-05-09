from stats import number_of_words
from stats import symbol_breakdown
from stats import sort_dictionaries
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as opened:
        text = opened.read()
    return text

def main(bookpath):
    frankenstein = get_book_text(bookpath)
    num = number_of_words(frankenstein)
    sym_dict = symbol_breakdown(frankenstein)
    char_list = sort_dictionaries(sym_dict)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}")
    print(f"----------- Word Count ----------")
    print(f"Found {num} total words")
    print(f"--------- Character Count -------")
    for char_dict in char_list:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print(f"============= END ===============")

    
main(sys.argv[1])
