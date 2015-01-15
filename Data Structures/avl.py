"""
-More testing should be done but, it seems to work just fine now
-If performance issues are encountered, amout of recalculating height
could be reduced (might be negligible)
-Docstrings could be added to helper function (to be decided later)
"""


class AVLNode():
    def __init__(self, data, left=None, right=None, height=0):
        self._data = data
        self._left = left
        self._right = right
        self._height = height

    def __repr__(self):
        return str(
            'AVLNode(' + str(self._data) + ', ' + repr(self._left) +
            ', ' + repr(self._right) + ', ' + repr(self._height) + ')'
        )


def _rotate_right(node):
    #rotating the node right
    root = node._left
    node._left = node._left._right
    root._right = node
    return root


def _rotate_left(node):
    #rotating the node left
    root = node._right
    node._right = node._right._left
    root._left = node
    return root


def _get_balance(node):
    #calculating left and right heights
    left_h = node._left._height if node._left is not None else -1
    right_h = node._right._height if node._right is not None else -1
    #updating the nodes height
    node._height = (left_h if left_h > right_h else right_h) + 1
    balance = left_h - right_h
    return balance


def _get_height(node):
    """NOT TO BE USED IN AVL CALCULATIONS.
    THIS IS ONLY FOR DEBUGGING PURPOSES."""
    left = 1 + _get_height(node._left) if node._left else 0
    right = 1 + _get_height(node._right) if node._right else 0
    return left if left > right else right


def _rebalance(node):
    #checking balance factors to follow avl rules
    balance = _get_balance(node)
    #finding how to rotate
    if balance < -1:
        if _get_balance(node._right) > 0:
            #right left case
            node._right = _rotate_right(node._right)
        #right right case
        node = _rotate_left(node)
    elif balance > 1:
        if _get_balance(node._left) < 0:
            #left right case
            node._left = _rotate_left(node._left)
        node = _rotate_right(node)
    else:
        return node
    #recalculating balance
    _get_balance(node._left)
    _get_balance(node._right)
    _get_balance(node)
    return node


def _visualize(node, indent=""):
        #prints the nodes data first
        print(indent + str(node._data))
        #recursively prints the right children's data (and then the same for
        #the left children) with each child having one more indent than
        #its parent
        if(node._right is not None):
            _visualize(node._right, indent + "\t")
        if(node._left is not None):
            _visualize(node._left, indent + "\t")


def inorder(node):
    '''
    (AVLNode) -> list
    Return a list of cargos in the tree using an inorder traversal
    >>> inorder(AVLNode(4, AVLNode(3, None, None), AVLNode(5, None, None)))
    [3, 4, 5]
    '''
    if node is None:
        return []
    else:
        return inorder(node._left) + [node._data] + inorder(node._right)


def insert(node, value):
    '''
    (AVLNode, int) -> AVLNode
    Return the root of the tree rooted at node after the node with value
    has been inserted into the tree with the AVL rules restored
    >>> root = AVLNode(5)
    >>> root = insert(root, 6)
    >>> root = insert(root, 7)
    >>> root
    AVLNode(6, AVLNode(5, None, None, 0), AVLNode(7, None, None, 0), 1)
    '''
    #doing a bst insert recursively
    #base case
    if node is None:
        return AVLNode(value)
    elif value <= node._data:
        #bst inserting in the left side recursively
        node._left = insert(node._left, value)
    else:
        #bst inserting in the right side recursively
        node._right = insert(node._right, value)
    #rebalancing
    return _rebalance(node)


def delete(node, value):
    '''
    (AVLNode, int) -> AVLNode
    Return the root of the AVL tree at node with the node containing the value
    removed.
    >>> root = AVLNode(2, AVLNode(1), AVLNode(3))
    >>> root = delete(root, 2)
    >>> root
    AVLNode(3, AVLNode(1, None, None, 0), None, 1)
    '''
    #base case
    if node is None or not (node._left or node._right):
        return
    elif value < node._data:
        node._left = delete(node._left, value)
    elif value > node._data:
        node._right = delete(node._right, value)
    #node has been found
    else:
        #picking closest element that is greater (in order successor)
        current = node._right
        while current and current._left and current._left._left:
            current = current._left
        #current is successor
        if not current._left:
            node._data = current._data
            node._right = current._right
        #current is parent of successor
        else:
            #overwriting nodes data with successor
            node._data = current._left._data
            current._left = current._left._right
            current = _rebalance(current)
    return _rebalance(node)


def convert_to_avl(array):
    '''
    (list) -> AVLNode
    Return a AVLNode with all elements from the list inserted
    >>> x = [2, 0, 1]
    >>> convert_to_avl(x)
    AVLNode(1, AVLNode(0, None, None, 0), AVLNode(2, None, None, 0), 1)
    '''
    #first element is made into the root of the tree
    root = AVLNode(array[0])
    #the rest of the elements are inserted into the avl tree
    for e in array[1:]:
        root = insert(root, e)
    return root


def avl_sort(array):
    '''
    (list) -> list
    Return a copy of the list that has been sorted using AVL sort
    >>> avl_sort([5, 7, 1, 4, 3, 2, 6])
    [1, 2, 3, 4, 5, 6, 7]
    '''
    root = convert_to_avl(array)
    return inorder(root)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
