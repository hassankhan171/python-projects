def tri():
    try:
        n = int(input("Enter the number: "))
        for i in range(1, n+1):
            print(str(i) * i)
    except Exception as e:
        print('Something went wrong')
        print('Error reason: ', e)

tri()