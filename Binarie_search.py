
import random


def Binarie_search(List_a, start, end, Object_o):

    print(f'Searching {Object_o} in {List_a[start]} and {List_a[end - 1]} ' )

    if start > end:
        return False

    half = (start + end ) // 2

    if List_a[half] == Object_o:
        return True

    elif List_a[half] < Object_o:
        return Binarie_search(List_a , half + 1, end, Object_o )

    else:
        return Binarie_search( List_a, start, half - 1, Object_o)


if __name__ == '__main__':

    list_size = int(input('How many numbers do u want on the list: '))
    Object = int(input('What is the number that u want to search: '))

    List = sorted([random.randint (0,100) for i in range(list_size) ])

    Found = Binarie_search(List,0,len (List), Object )
    print(List)
    print( f'The element {Object} {"is" if Found else "is not" } on the list ' )
