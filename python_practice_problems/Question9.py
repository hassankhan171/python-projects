# Problem No 9
'''
Complete the function that accepts a string parameter, and reverses each word in the
string. All spaces in the string should be retained.
"This is an example!" ==> "sihT si na !elpmaxe"
"double spaces" ==> "elbuod secaps" '''

# solution

try:
    word = input("Enter the words:  ")
    n = len(word)
    a = []
    for i in range(n-1, -1, -1):
        a.append(word[i])
    print("".join(a))
except Exception as e:
    print('Something went wrong')
    print('Error reason: ', e)

