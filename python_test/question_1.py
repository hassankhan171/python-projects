
def create_unique_words():
        try:
            n = int(input("Enter the number of words: "))
            words = []
            for i in range(1, n+1):
                word = input(f"Enter the word {i}: ").lower()
                words.append(word)
            unique_words = set(words)
            print("Unique words:", unique_words)
            print("Total unique words:", len(unique_words))

            word_count = {}   # Empty Dictionary
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

            for word, count in word_count.items():
                print(f"{word}: {count}")

            return word_count
        except Exception as e:
            print('Something went wrong')
            print('Error reason: ', e)

create_unique_words()
