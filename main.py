import sys
from stats import count_words
from stats import count_characters
from stats import sorted_report

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")

    text = get_book_text(path)
    book_words = count_words(text)
    print (f"Found {book_words} total words")
    print("--------- Character Count -------")
    characters = count_characters(text)
    sorted_text = sorted_report(characters)
    for item in sorted_text:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()