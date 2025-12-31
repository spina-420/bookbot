from stats import get_num_words, letter_count, report
import sys

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    count = letter_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")    
    print("--------- Character Count -------")   
    for letter in report(count):
        print(letter["char"]+": " + str(letter["num"]))    
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()

