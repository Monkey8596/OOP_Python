
import random


def Lineal_search(list_a, object_a):

    match = False

    for elemento in list_a:
        if elemento == object_a:
            match = True
            break
    return match

if __name__ == '__main__':

    list_size = int(input('How many numbers do u want on the list: '))
    Object = int(input('What is the number that u want to search: '))

    List = [random.randint (0,100) for i in range(list_size) ]

    Found = Lineal_search(List, Object)
    print(List)
    print( f'The element {Object} {"is" if Found else "is not" } on the list ' )





