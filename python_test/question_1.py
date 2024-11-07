def create_unique_words():
    try:
        n = int(input("Enter the number of words: "))
        print("--------------------------------")
        words = []
        for i in range(1, n + 1):
            word = input(f"Enter the word {i}: ").lower()
            words.append(word)
        unique_words = set(words)
        print("--------------------------------")
        print("Unique words: ", unique_words)
        print("Total unique words: ", len(unique_words))
        print("--------------------------------")

        word_count = {}  # Empty Dictionary
        for a in words:
            if a in word_count:
                word_count[a] += 1
            else:
                word_count[a] = 1

        for a, count in word_count.items():
            print(f"{a}: {count}")

        return word_count
    except Exception as e:
        print('Something went wrong')
        print('Error reason: ', e)


create_unique_words()
