# Problem No 1
'''
Write a function which will take an integer as input and print each digit in a separate
line. You are not allowed to use str or any other method will convert the integer into
string.
Input: 1011
Output:
1
1
0
1
'''

number = input("Enter the number: ")
n = len(number)
print(f"Total digits in the number: {n} ")
for i in range(n):
    print(number[i])

