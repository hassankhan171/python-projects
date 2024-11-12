# Problem No 04
'''
You are given a string. Suppose a character ‘c’ occurs 4 times in the string. Replace
these consecutive occurrences of the character 'c' with (4, c) in the string.
Input format: A single line of input consisting of string s
Output format: A single line of output consisting of the modified string.
Input:
1222311
Output:
(1, 1) (3, 2) (1, 3) (2, 1)
'''

def consecutive_occurrence():
    try:
        word = input("Enter the Word or Number: ").lower()
        n = len(word)
        count = 1
        for i in range(n-1):
            if word[i] == word[i+1]:
                count += 1
            else:
                print((count, word[i]))
                count = 1
        print((count, word[-1])) # to print the occurrence of the last character
    except Exception as e:
        print('Something went wrong')
        print('Error reason: ', e)

consecutive_occurrence()