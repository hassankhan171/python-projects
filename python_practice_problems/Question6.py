# Problem No 6

#You get an array of numbers, and return the sum of all the positive ones. Example
#[1, -4, 7, 12] => 1+7+12 = 20. If there is nothing to sum return 0. You can not use the
#if statement.

# solution
try:
    numbers = [1, -4, 7, 12]
    n = len(numbers)
    sum_pos = 0
    for i in range(n):
        if numbers[i]>0:
            sum_pos = sum_pos + numbers[i]
    print(sum_pos)
except Exception as e:
    print('Something went wrong')
    print('Error reason: ', e)
