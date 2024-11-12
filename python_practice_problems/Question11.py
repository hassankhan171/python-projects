# Problem No 11
'''
You are given an array(list) strarr of strings and an integer k. Your task is to return the
first longest string consisting of k consecutive strings taken in the array.
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2
Concatenate the consecutive strings of strarr by 2, we get:
treefoling (length 10) concatenation of strarr[0] and strarr[1]
folingtrashy (" 12) concatenation of strarr[1] and strarr[2]
trashyblue (" 10) concatenation of strarr[2] and strarr[3]
blueabcdef (" 10) concatenation of strarr[3] and strarr[4]
abcdefuvwxyz (" 12) concatenation of strarr[4] and strarr[5]
Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so
longest_consec(strarr, 2) should return "folingtrashy".
'''

# Solution
try:
    strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"]
    n = len(strarr)
    print("----------------------------------------------")
    print("Total number of words = ", n)
    print("----------------------------------------------")
    print(f"The total number of words after combining = {n-1}")
    print("----------------------------------------------")
    st = []
    comb = []
    for i in range(n-1):
        comb = strarr[i] + strarr[i+1]
        st.append(comb)
        print(f"{i+1}- {st[i]}")

    maxi = max(st, key=len)
    max_index = st.index(maxi)
    print("----------------------------------------------")
    print(f"The longest string is: {maxi} at index: {max_index}")
except Exception as e:
    print('Something went wrong')
    print('Error reason: ', e)

