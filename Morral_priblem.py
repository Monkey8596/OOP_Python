
def Morral(size, weigth, values,n ):
    
    if n == 0 or size == 0:
        return 0
    

    print('*'*20)

    if weigth[n-1] > size:
        print('Se cumplio el if')
        print(weigth[n-1])
        print(n - 1)
        return Morral(size, weigth, values,n -1 )
    

    # print(values[n-1])
    # print('*'*20)

    # print(size - weigth[n-1])
    # print('*'*20)

    # print(weigth, values,n -1)
    # print('*'*20)

    # print(Morral(size - weigth[n-1], weigth, values,n -1 ))
    # print('*'*20)

    print(values[n-1], 'values [n-1]')

    # print(Morral(size - weigth[n-1], weigth, values,n -1 ) , 'segunda parte (size - weigth)')

    print('*'*20)

    return max(values[n-1]+ Morral(size - weigth[n-1], weigth, values,n -1 ),
                Morral(size, weigth, values,n -1 ))




if __name__ == '__main__':
    values = [60,100,120]
    weigth = [10,20,30]
    size = 50
    n = len(values)

    result = Morral(size, weigth, values,n )
    print(result)

