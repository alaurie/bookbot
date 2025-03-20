def get_book_text(book):
    with open(book) as b:
        book_contents = b.read()
        return book_contents


def count_words(book_contents):
    num_words = len(book_contents.split())
    print(f"Found {num_words} total words")


def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def print_character_report(char_counts):
    for k,v in sorted(char_counts.items()):
        print(f"{k}: {v}")
