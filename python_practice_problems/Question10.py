#You are going to be given a word. Your job is to return the middle character of the
#word. If the word's length is odd, return the middle character. If the word's length is
#even, return the middle 2 characters.
#test => es
#testing => t

try:
    word = input("Enter The Word: ")
    n = len(word)
    print("----------")
    print(f"Total {n} characters")
    if n%2 == 0:
        print("It is an Even number")
        print("----------")
        print(word[n//2 - 1], word[n//2])
    else:
        print("It is an Odd number")
        print("----------")
        print(word[(n-1)//2])
except Exception as e:
    print('Something went wrong')
    print('Error reason: ', e)




