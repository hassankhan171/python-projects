from collections import Counter

def create_unique_words():
        words = input("Enter the words: ").lower().split()
        unique_words = set(words)
        print("Unique words:", unique_words)
        print("Total unique words:", len(unique_words))

        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        for word, count in word_count.items():
            print(f"{word}: {count}")

        return word_count


create_unique_words()
