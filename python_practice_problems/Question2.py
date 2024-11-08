#Problem No 2
'''
You are given words. Some words may repeat. For each word, output its number of
occurrences. The output order should correspond with the input order of appearance
of the word. See the sample input/output for clarification.
Input format: two parameters: first number of words, second list of words to process
Output format: Output two lines
First line: Number of unique words
Second line: Number of occurrences for each distinct word according to their
appearance in the input.
Input:
4, [“bcdef”, “abcdefg”, “bcde”, “bcdef”]
Output:
3
2 1 1
Output explanation:
First output distinct words.
Second line shows the count for each word which occurred in the list
'''

# solution

def create_unique_words():
        try:
            n = int(input("Enter the number of words: "))
            print("--------------------------------")
            words = []
            for i in range(1, n+1):
                word = input(f"Enter the word {i}: ").lower()
                words.append(word)
            unique_words = set(words)
            print("--------------------------------")
            print("Unique words: ", unique_words)
            print("Total unique words: ", len(unique_words))
            print("--------------------------------")

            word_count = {}   # Empty Dictionary
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
