def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    converted = text.lower()

    for letter in converted:
        if letter not in char_counts:
            char_counts[letter] = {
                "char": letter,
                "num": 1
            }
        else:
            char_counts[letter]["num"] += 1
    return char_counts

 def sorted_characters(text):
    def sort_on(items):
       return items[1]["num"]
    unsorted = count_characters(text)
    items = unsorted.items()
    sorted_dict = sorted(items, reverse=True, key=sort_on)
    return sorted_dict


        

