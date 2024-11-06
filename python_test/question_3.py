def reverse_word():
    try:
        word = input("Enter a word: ")
        reversed_word = word[::-1]
        print("Reversed word:", reversed_word)

        if reversed_word == word:
            print("The Given Word is a Palindrome ")
        else:
            print("The Given Word is not a Palindrome ")
    except Exception as e:
        print('Something went wrong')
        print('Error reason: ', e)

reverse_word()
