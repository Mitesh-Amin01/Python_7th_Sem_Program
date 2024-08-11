def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()

        words = text.split()

        num_words = len(words)

        print(f"The number of words in the file is: {num_words}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

filename = 'output.txt' 
count_words_in_file(filename)
