from stats import count_words, get_book_text, count_characters, print_character_report
import sys

def main():
    # Check if we have correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    print("============ BOOKBOT ============ ")
    print("Analyzing book found at books/frankenstein.txt...")
    text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    count_words(text)
    char_counts = count_characters(text)
    print("--------- Character Count -------")
    print_character_report(char_counts)
    print("============= END ===============")

main()