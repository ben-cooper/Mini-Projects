from random import random, randint


class Treap():
    def __init__(self, cargo, left=None, right=None, priority='rand'):
        self._cargo = cargo
        self._priority = random() if priority == 'rand' else priority
        self._left = left
        self._right = right

    def __repr__(self):
        return str(
            'Treap(' + str(self._cargo) + ', ' + repr(self._left) +
            ', ' + repr(self._right) + ', ' + repr(self._priority) + ')'
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


def insert(node, value, priority='rand'):
    '''
    (Treap, int, int) -> Treap
    Return the root of the tree rooted at node after the node with value
    has been inserted into the tree
    '''
    #base case
    if node is None:
        return Treap(value, priority=priority)
    elif value <= node._cargo:
        #bst inserting into left side
        node._left = insert(node._left, value, priority)
        #rotating to maintain min heap property as necessary
        if node._priority > node._left._priority:
            node = node._rotate_right()
    else:
        #bst inserting into right side
        node._right = insert(node._right, value, priority)
        #rotating to maintain min heap property as necessary
        if node._priority > node._right._priority:
            node = node._rotate_left()
    return node


def delete(root, value):
    '''
    (Treap, int) -> Treap
    Return the root of the tree rooted at root with the node containing value
    deleted from the tree
    '''
    #base case
    if root is None:
        return None
    #seeing if root is value
    if value == root._cargo:
        #base case
        if root._left is None and root._right is None:
            return None
        #no right child or left has lower priority then right
        #means rotate left
        elif (
            root._left is None or
            (root._right is not None and
                root._left._priority > root._right._priority)
        ):
            root = root._rotate_left()
            root._left = delete(root._left, value)
        #no left child or right has lower priority then left
        #means rotate right
        else:
            root = root._rotate_right()
            root._right = delete(root._right, value)
    elif value < root._cargo:
        root._left = delete(root._left, value)
    else:
        root._right = delete(root._right, value)
    return root


def inorder(node):
    '''
    (Treap) -> list
    Return a list of cargos in the tree using an inorder traversal
    >>> inorder(Treap(4, Treap(3, None, None), Treap(5, None, None)))
    [3, 4, 5]
    '''
    if node is None:
        return []
    else:
        return inorder(node._left) + [node._cargo] + inorder(node._right)


def treapify(array):
    '''
    (list) -> Treap
    Return a Treap with all elements from the list inserted
    '''
    root = Treap(array[0])
    for e in array[1:]:
        root = insert(root, e)
    return root


def treap_sort(array):
    '''
    (list, bool) -> list
    Return a copy of the list that has been sorted using treap sort
    and destroy the list if destroy is True
    >>> treap_sort([5, 7, 1, 4, 3, 2, 6])
    [1, 2, 3, 4, 5, 6, 7]
    '''
    root = treapify(array)
    return inorder(root)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
