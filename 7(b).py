import re
from collections import Counter

def most_frequent_words(filename, num_words=10):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        words = re.findall(r'\w+', text.lower())

        word_counts = Counter(words)

        most_common_words = word_counts.most_common(num_words)

        print(f"The {num_words} most frequent words in the file are:")
        for word, count in most_common_words:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = 'output.txt' 
most_frequent_words(filename, num_words=10)
