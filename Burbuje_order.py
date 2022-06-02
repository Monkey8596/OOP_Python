
import random


def Burbuje_order(lista):

    n = len(lista)

    for i in range(n):
        for j in range (0, n - i - 1):

            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


if __name__ == '__main__':

    list_size = int(input('How many numbers do u want on the list: '))

    List = [random.randint (0,100) for i in range(list_size) ]
    print(List)

    Order_list = Burbuje_order(List)
    print(Order_list)