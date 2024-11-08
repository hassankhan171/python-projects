# # Problem No 03
'''
You are given a positive integer. You can only use one for loop and one print
statement. Print a numerical triangle of height like the one below:
Input:
5
Output:
1
22
333
4444
55555
'''

# solution

def tri():
    try:
        n = int(input("Enter the number: "))
        for i in range(1, n+1):
            print(str(i) * i)
    except Exception as e:
        print('Something went wrong')
        print('Error reason: ', e)

tri()