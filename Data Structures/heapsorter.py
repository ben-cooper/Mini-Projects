class HeapNode():
    def __init__(self, cargo, left=None, right=None, num_nodes=1):
        self._cargo = cargo
        self._left = left
        self._right = right
        self._num_nodes = 1


def insert(root, new):
    '''
    (HeapNode, int) -> HeapNode
    Return the HeapNode with the new integer inserted into the tree while
    maintaining the min heap property
    >>> root = HeapNode(5)
    >>> ignore = insert(root, 4)
    >>> root._cargo
    4
    >>> root._left._cargo
    5
    '''
    #base case is if the root is None
    if root is None:
        result = HeapNode(new)
    else:
        #incrementing node count
        root._num_nodes += 1
        #swapping root value and new value if new value is smaller than root
        if new < root._cargo:
            new, root._cargo = root._cargo, new
        #counting the number of nodes on each side of the tree
        left_nodes = 0 if root._left is None else root._left._num_nodes
        right_nodes = 0 if root._right is None else root._right._num_nodes
        #if there are less nodes on the left then the new node is inserted on
        #the left side of the tree, otherwise it is inserted on the right side
        #of the tree
        if left_nodes <= right_nodes:
            root._left = insert(root._left, new)
        else:
            root._right = insert(root._right, new)
        result = root
    return result


def delete_root(root):
    '''
    (HeapNode) -> HeapNode
    Return the HeapNode with the root deleted
    >>> root = HeapNode(5)
    >>> ignore = insert(root, 3)
    >>> ignore = insert(root, 4)
    >>> ignore = delete_root(root)
    >>> root._cargo
    4
    '''
    #returning the other child if one is None
    if root._left is None:
        result = root._right
    elif root._right is None:
        result = root._left
    else:
        #decreasing node counter
        root._num_nodes -= 1
        #replacing root with appropriate successor then replacing its children
        #with appropriate successors recursively
        if root._left._cargo <= root._right._cargo:
            root._cargo = root._left._cargo
            root._left = delete_root(root._left)
        else:
            root._cargo = root._right._cargo
            root._right = delete_root(root._right)
        result = root
    return result


def heap_sort(array):
    '''
    (list) -> list
    Return a sorted version of the list array without mutation
    >>> x = [5, 1, 4, 3, 2]
    >>> heap_sort(x)
    [1, 2, 3, 4, 5]
    >>> x
    [5, 1, 4, 3, 2]
    '''
    #creating heap (min)
    heap = HeapNode(array[0])
    for e in array[1:]:
        insert(heap, e)
    #inserting elements from heap into list by adding the root's cargo then
    #deleting the root
    result = []
    while heap is not None:
        result.append(heap._cargo)
        heap = delete_root(heap)
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
