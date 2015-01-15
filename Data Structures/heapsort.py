def heapify(array):
    '''
    (list) -> list
    Mutate the list such that is satisfies the heap property
    >>> x = [6, 1, 4, 2, 3, 5]
    >>> heapify(x)
    >>> x
    [6, 3, 5, 1, 2, 4]
    '''
    length = 1
    #assume part of the list is a heap, bubble the first non heap element
    #array[length] will be the next element
    while length < len(array):
        current = length
        parent = (length - 1) // 2
        #bubbling up next element not part of heap
        while array[current] > array[parent]:
            array[current], array[parent] = array[parent], array[current]
            current = parent
            parent = (current - 1) // 2 if current > 0 else 0
        #heapifying next element
        length += 1


def bubble_down(array, index, stop=False):
    '''
    (list, int, int) -> list
    Bubble down the element at the index until it no longer violates the heap
    property
    >>> x = [5, 1, 2, 3, 4]
    >>> bubble_down(x, 1)
    >>> x
    [5, 4, 2, 3, 1]
    '''
    exit = False
    stop = len(array) if not stop else stop
    while not exit and index * 2 + 1 < stop:
        #finding child to swap with
        left = index * 2 + 1
        right = index * 2 + 2 if index * 2 + 2 < stop else False
        max_index = left if not right or array[left] > array[right] else right
        #seeing if bubble down is needed
        if array[index] < array[max_index]:
            array[index], array[max_index] = array[max_index], array[index]
            index = max_index
        else:
            exit = True

def heapsort(array):
    '''
    (list) -> list
    Mutate the list such that it is heap sorted
    >>> x = [6, 1, 4, 2, 3, 5]
    >>> heapsort(x)
    >>> x
    [1, 2, 3, 4, 5, 6]
    '''
    heapify(array)
    count = len(array) - 1
    while count > 0:
        array[0], array[count] = array[count], array[0]
        bubble_down(array, 0, count)
        count -= 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
