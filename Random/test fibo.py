'''
def fibo(n):
    """
    (int) -> int
    Return the value of the nth fibonacci sequence
    >>> fibo(10)
    55
    """
    #base case
    if n <=2:
        result = 1
    else:
        #this is done for efficiency
        result = fibo(n-1) + fibo(n-2)
    return result
'''
#iterative
def fibo(n):
    if n <= 2:
        return 1
    else:
        new = 1
        old = 1
        for i in range(1, n-2):
            new, old = new + old, new
        return new + old

#recursive
def fibor(n):
    return 1 if n <= 2 else fibor(n-1) + fibor(n-2)

#iterative v2:
def fibot(n):
    new, old = 1, 1
    for i in range(3, n+1):
        new, old = new + old, new
    return new
