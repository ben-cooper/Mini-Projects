class SplayNode():
    def __init__(self, data, left=None, right=None):
        self._data = data
        self._left = left
        self._right = right

    def __repr__(self):
        return str(
            'SplayNode(' + str(self._data) + ', ' + repr(self._left) +
            ', ' + repr(self._right) + ')'
        )

    def _rotate_right(self):
        root = self._left
        self._left = self._left._right
        root._right = self
        return root

    def _rotate_left(self):
        root = self._right
        self._right = self._right._left
        root._left = self
        return root

    def get_height(self):
        left = 1 + self._left.get_height() if self._left else 0
        right = 1 + self._right.get_height() if self._right else 0
        return left if left > right else right


def inorder(node):
    '''
    (SplayNode) -> list
    Return a list of cargos in the tree using an inorder traversal
    >>> inorder(SplayNode(4, SplayNode(3), SplayNode(5)))
    [3, 4, 5]
    '''
    if node is None:
        return []
    else:
        return inorder(node._left) + [node._data] + inorder(node._right)


def insert(node, value, root=True):
    '''
    (SplayNode) -> SplayNode
    Return the node with a node containing value inserted into the tree after
    splaying the node being inserted
    >>> x = SplayNode(2)
    >>> x = insert(x, 0)
    >>> x = insert(x, 1)
    >>> x
    SplayNode(1, SplayNode(0, None, None), SplayNode(2, None, None))
    '''
    #doing bst insert then finding parents and grandparents
    if node is None:
        return SplayNode(value)
    if value <= node._data:
        node._left = insert(node._left, value, False)
        #checking if the node is a grandparent node (lazy eval)
        if node._left._right is not None and node._left._right._data == value:
            #zig zag
            node._left = node._left._rotate_left()
            node = node._rotate_right()
        elif node._left._left is not None and node._left._left._data == value:
            #zig zig
            node = node._rotate_right()._rotate_right()
    else:
        node._right = insert(node._right, value, False)
        #checking if the node is a grandparent node (lazy eval)
        if node._right._left is not None and node._right._left._data == value:
            #zig zag
            node._right = node._right._rotate_right()
            node = node._rotate_left()
        elif (node._right._right is not None and
                node._right._right._data == value):
            #zig zig
            node = node._rotate_left()._rotate_left()
    #zig step if needed (lazy eval)
    if root and node._left is not None and node._left._data == value:
        #zig
        node = node._rotate_right()
    elif root and node._right is not None and node._right._data == value:
        #zig
        node = node._rotate_left()
    return node


def splayify(array):
    '''
    (list) -> SplayNode
    Return a SplayNode with all elements from the list inserted
    >>> x = [2, 0, 1]
    >>> splayify(x)
    SplayNode(1, SplayNode(0, None, None), SplayNode(2, None, None))
    '''
    root = SplayNode(array[0])
    for e in array[1:]:
        root = insert(root, e)
    return root


def splay_sort(array):
    '''
    (list) -> list
    Return a copy of the list that has been sorted using splay sort
    >>> splay_sort([5, 7, 1, 4, 3, 2, 6])
    [1, 2, 3, 4, 5, 6, 7]
    '''
    root = splayify(array)
    return inorder(root)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
