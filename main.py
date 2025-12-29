from stats import count_words, count_characters, sorted_characters
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    topper = "============ BOOKBOT ============"
    analyzer = f"Analyzing book found at {filepath}..."
    word_count_topper = "----------- Word Count ----------"
    character_count_topper = "--------- Character Count -------"
    closer = "============= END ==============="
    text = get_book_text(filepath)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_chars = sorted_characters(text)
    lines = []
    for char, num in sorted_chars:
        if char.isalpha():
            lines.append(f"{char}: {num['num']}")
    sorted_chars = "\n".join(lines)

    print(topper + "\n"
          + analyzer + "\n"
          + word_count_topper + "\n"
          + f"Found {num_words} total words \n"
          + character_count_topper + "\n"
          + sorted_chars + "\n"
          + closer)

main()